from rest_framework import serializers
from materials.models import Polymer, Producer,Product, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    #polymer_name = serializers.StringRelatedField()
    #producer_name =serializers.StringRelatedField() 
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        myrec = Product.objects.create(**validated_data)
        poy = Polymer.objects.filter(polymer_name = validated_data["polymer"])
        pod = Producer.objects.filter(producer_name= validated_data["producer"])

        myrec.polymer = poy[0]
        myrec.product = pod[0]
        myrec.save()
        return myrec

    def update(self, instance, validated_data):
        poy = Polymer.objects.filter(polymer_name = validated_data["polymer"])
        pod = Producer.objects.filter(producer_name= validated_data["producer"])
        if(poy != []):
            instance.polymer = poy[0]
            print "polymer:" ,poy[0] 
        if(pod != []):
            instance.producer = pod[0]
            print "producer:" ,pod[0]

        #instance.producer = validated_data("producer", instance.producer)
        #instance.polymer = validated_data('polymer', instance.polymer)
        instance.grade_name = validated_data.get('grade_name', instance.grade_name)
        instance.mold_temperature = validated_data.get('mold_temperature' , instance.mold_temperature)
        instance.melt_temperature = validated_data.get('melt_temperature', instance.melt_temperature)
        instance.save()
        return instance
        #We will let the user update their username and tagline attributes for now. If these keys are present in the arrays dictionary, we will use the new value. Otherwise, the current value of the instance object is used. Here, instance is of type Account.
class ProducerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Producer
        fields = ('url', 'id','producer_name','owner')

    def create(self, validated_data):
        producer_name = Producer.objects.create(**validated_data)
        return producer_name

    def update(self, instance, validated_data):
        instance.producer_name = validated_data.get('producer_name', instance.producer_name)
        instance.save()
        return instance


class PolymerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:       
        model = Polymer
        fields = '__all__'

    def create(self, validated_data):
        polymer_name = Polymer.objects.create(**validated_data)
        return polymer_name

    def update(self, instance, validated_data):
        instance.polymer_name = validated_data.get('polymer_name', instance.polymer_name)
        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    polymers = serializers.HyperlinkedRelatedField(many=True, view_name='polymer-detail', read_only = True)
    producers = serializers.HyperlinkedRelatedField(many=True,view_name='producer-detail', read_only = True)
    products = serializers.HyperlinkedRelatedField(many=True,  view_name='product-detail', read_only = True)
    class Meta:
        model = User
        fields = ('id', 'username', 'polymers', 'producers', 'products')