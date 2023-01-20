from django import forms


from account.models import User	
# Create your forms here.

#=================== Register Form =======================================================
TYPE_CHOICE = (
            ("OWNER", "OWNER"),
            ("CUSTOMER", "CUSTOMER")
            )
class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required = True,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(required = True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required = True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    address = forms.CharField(required = True,widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile_number = forms.IntegerField(required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(required = False, widget=forms.DateInput(attrs={'class':'form-control'}))

    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password=forms.CharField(max_length=16,widget=forms.PasswordInput())
    user_type= forms.CharField(required = True,label='Chocie your Role', widget=forms.Select(choices=TYPE_CHOICE))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 
            'mobile_number', 'date_of_birth','user_type', 'address')
        
  
    
    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        
        super(UserRegisterForm, self).clean()
        
        # extract the username and text field from the data
        mobile_number = self.cleaned_data.get('mobile_number')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")


        if password != confirm_password:
            self._errors['password'] = self.error_class([
                "Password and Confirm password does not match"])
        

        # Done
        if User.objects.filter(email=email):
            self._errors['email'] = self.error_class([
                "This email address is already in use. Please supply a different email address."])
        

        if User.objects.filter(username=username):
            self._errors['username'] = self.error_class([
                "This Username address is already in use. Please supply a different Username address."])
      
        # Mobile Number
        if User.objects.filter(mobile_number=mobile_number):
            self._errors['mobile_number'] = self.error_class([
                "This Mobile number  is already in use. Please supply a different Mobile number."])

        

        # Done 
        if not first_name.isalpha():
            self._errors['first_name'] = self.error_class([
                'First Name should in Only Alphabet'])

        if not last_name.isalpha():
            self._errors['last_name'] = self.error_class([
                'Last Name should in Only Alphabet'])
        
        return self.cleaned_data

    
        
    
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


#=================== Login Form =======================================================
# from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.CharField(required = True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password']

    

#=================== User Update Form ======================================================= 
   
class UpdateUserForm(forms.ModelForm):

    username = forms.CharField(required=True,
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(required = False, widget=forms.DateInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User()
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile_number', 'date_of_birth','address']
        # fields = ['username', 'email']
