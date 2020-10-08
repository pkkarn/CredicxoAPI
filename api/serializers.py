from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Creating Serailizer for Registeration(SignUp)


class RegisterationSerializer(serializers.ModelSerializer):
    role_choice = (
        ('super-admin', 'super-admin'),
        ('teacher', 'teacher'),
        ('student', 'student')
    )
    role = serializers.ChoiceField(choices=role_choice)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)  # Defining Extra Field, Because django User mode has only one password field

    class Meta:
        model = User
        fields = ['email', 'username', 'password',
                  'password2', 'role', 'groups']
        extra_kwargs = {
            # For Security, So that after creating an Account User can't read it.
            'password': {'write_only': True}
        }

    def save(self):   # For Password Verification, we're overiding defauly save() method
        user_acc = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        role = self.validated_data['role']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Password didn\'t match '})
        user_acc.set_password(password)
        user_acc.save()
        # After Save adding Group
        group = Group.objects.get(name=role)
        user_acc.groups.add(group)

        return user_acc


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
        # Group - 1-Teacher, 2-student, 3-super-admin
