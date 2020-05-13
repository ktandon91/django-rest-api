
# 1. Serializers work the same way as forms in django
# 2. To validate data in forms user keyword 'clean'
# 3. To validate data in serializers use keyword 'validate', with function
#     having first argument as self and second actual value passed to the serializer for that (field)
# 4. Before saving always check is_valid method.
# 5. include the app in settings
# 6. to include urls that are used in app, do not import app directly,
# instead use include function provided in url package of django

# 7. Instead of having separate views for CRUD, logical groupping can be done
# 8. List & create can be handled in one view, whereas rest of the operations DELETE, PUT, DETAIL
# can be grouped together, since later 3 work on a single element and it's logical to group them together.
#generics views have separate classed for CRUD mixins can be used to club operations together
#9. ALL CRUD CAN BE used in a single class
#10. UPDATE/DESTROY mixins with DETAIL generic is same as generics RetriveUpdateDestroyAPIView all do the same thing
#11. global permissions and authentication method can be declared in REST_FRAMEWORK global variable in settings
#12. Getting to setup jwt, install djangorestframework-jwt library set a url at auth app level or project level
#13. from rest_framework_jwt.views import obtain_jwt_token to get the token and in REST_FRAMEWORK variable of settings
# under default authentication classes add     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',

#14. overwriting a field in serializer with property write only will not display that field in json output.
# required for passwords, since we do not want to show these to the outside world

# 15. to create restricted access, create gropups and associate users with appropriate groups
#16. Then create custom permission and overwrite has_permission method and check for the group
