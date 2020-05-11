from rest_framework import serializers
from .models import CourseSections, CourseSchedule, CourseSelections


class CourseScheduleSerializer(serializers.Serializer):
    ders_kod = serializers.CharField(max_length=20, blank=True, null=True)
    year = serializers.FloatField(blank=True, null=True)
    term = serializers.FloatField(blank=True, null=True)
    ders_s_id = serializers.FloatField(blank=True, null=True)
    section = serializers.CharField(max_length=20, blank=True, null=True)
    min_start_time = serializers.CharField(max_length=50, blank=True, null=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CourseSchedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.ders_kod = validated_data.get('ders_kod', instance.ders_kod)
        instance.year = validated_data.get('year', instance.year)
        instance.term = validated_data.get('term', instance.term)
        instance.ders_s_id = validated_data.get('ders_s_id', instance.ders_s_id)
        instance.section = validated_data.get('section', instance.section)
        instance.min_start_time = validated_data.get('min_start_time',instance.min_start_time)
        instance.save()
        return instance



class CourseSectionsSerializer(serializers.Serializer):
    ders_sobe_id = serializers.FloatField(blank=True, null=True)
    ders_kod = serializers.CharField(max_length=20, blank=True, null=True)
    year = serializers.FloatField(blank=True, null=True)
    term = serializers.FloatField(blank=True, null=True)
    section = serializers.CharField(max_length=20, blank=True, null=True)
    type = serializers.CharField(max_length=20, blank=True, null=True)
    emp_id = serializers.FloatField(blank=True, null=True)
    message = serializers.CharField(max_length=300, blank=True, null=True)
    week_num = serializers.FloatField(blank=True, null=True)
    hour_num = serializers.FloatField(blank=True, null=True)
    emp_id_ent = serializers.FloatField(blank=True, null=True)
    last_modified = serializers.CharField(max_length=50, blank=True, null=True)
    credits = serializers.FloatField(blank=True, null=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CourseSchedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.ders_sobe_id = validated_data.get('ders_sobe_id', instance.ders_sobe_id)
        instance.ders_kod = validated_data.get('ders_kod', instance.ders_kod)
        instance.year = validated_data.get('year', instance.year)
        instance.term = validated_data.get('term', instance.term)
        instance.section = validated_data.get('section', instance.section)
        instance.type = validated_data.get('type',instance.type)
        instance.emp_id = validated_data.get('emp_id', instance.emp_id)
        instance.message = validated_data.get('message', instance.message)
        instance.week_num = validated_data.get('week_num', instance.week_num)
        instance.hour_num = validated_data.get('hour_num', instance.hour_num)
        instance.emp_id_ent = validated_data.get('emp_id_ent', instance.emp_id_ent)
        instance.last_modified = validated_data.get('last_modified', instance.last_modified)
        instance.credits = validated_data.get('credits', instance.credits)
        instance.save()
        return instance


class CourseSelectionSerializer(serializers.Serializer):
    stud_id = serializers.CharField(max_length=50, blank=True, null=True)
    ders_kod = serializers.CharField(max_length=20, blank=True, null=True)
    year = serializers.FloatField(blank=True, null=True)
    term = serializers.FloatField(blank=True, null=True)
    section = serializers.CharField(max_length=20, blank=True, null=True)
    qiymet_yuz = serializers.FloatField(blank=True, null=True)
    qiymet_herf = serializers.CharField(max_length=20, blank=True, null=True)
    grading_type = serializers.CharField(max_length=20, blank=True, null=True)
    practice = serializers.FloatField(blank=True, null=True)
    reg_date = serializers.CharField(max_length=50, blank=True, null=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CourseSchedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.stud_id = validated_data.get('stud_id', instance.stud_id)
        instance.ders_kod = validated_data.get('ders_kod', instance.ders_kod)
        instance.year = validated_data.get('year', instance.year)
        instance.term = validated_data.get('term', instance.term)
        instance.section = validated_data.get('section', instance.section)
        instance.qiymet_yuz = validated_data.get('qiymet_yuz',instance.qiymet_yuz)
        instance.qiymet_herf = validated_data.get('qiymet_herf', instance.qiymet_herf)
        instance.grading_type = validated_data.get('grading_type', instance.grading_type)
        instance.practice = validated_data.get('practice', instance.practice)
        instance.reg_date = validated_data.get('reg_date', instance.reg_date)
        instance.save()
        return instance