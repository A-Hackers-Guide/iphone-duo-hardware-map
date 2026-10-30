# `DSSafetyCheckWhenBlocking`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"DSXPCSharingPermissions" _permissions;
@"HKMedicalIDStore" _medicalIDStore;
```

## Properties

```
@property (T@"DSXPCSharingPermissions",&,N,V_permissions) permissions;
@property (T@"HKMedicalIDStore",&,N,V_medicalIDStore) medicalIDStore;
```

## Class methods

```
+[DSSafetyCheckWhenBlocking featureEnabled];
```

## Instance methods

```
-[DSSafetyCheckWhenBlocking setPermissions:];
-[DSSafetyCheckWhenBlocking init];
-[DSSafetyCheckWhenBlocking medicalIDStore];
-[DSSafetyCheckWhenBlocking permissions];
-[DSSafetyCheckWhenBlocking setMedicalIDStore:];
-[DSSafetyCheckWhenBlocking removeEmergencyContact:completion:];
-[DSSafetyCheckWhenBlocking fetchSharingWithCompletion:];
-[DSSafetyCheckWhenBlocking startManageSharingWithContact:completion:];
-[DSSafetyCheckWhenBlocking isFetchNeeded];
-[DSSafetyCheckWhenBlocking _safetyCheckControllerWithPreview:forFetchResult:completion:];
-[DSSafetyCheckWhenBlocking emergencyContactForContacts:completion:];
-[DSSafetyCheckWhenBlocking emergencyContactForSharingPeople:completion:];
-[DSSafetyCheckWhenBlocking isSharingWith:completion:];
-[DSSafetyCheckWhenBlocking isSharingWithContacts:completion:];
-[DSSafetyCheckWhenBlocking removeEmergencyContactFromResult:andCreateUIWithCompletion:];
-[DSSafetyCheckWhenBlocking safetyCheckControllerWithPreview:forFetchResult:completion:];
```
