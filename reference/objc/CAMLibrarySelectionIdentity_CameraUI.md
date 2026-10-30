# `CAMLibrarySelectionIdentity`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMLibrarySelectionIdentityProtocol`
- 3 instance variables, 3 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"NSString" _phoneNumber;
@"NSString" _emailAddress;
@"NSArray" _contactIdentifiers;
```

## Properties

```
@property (T@"NSString",R,V_phoneNumber) phoneNumber;
@property (T@"NSString",R,V_emailAddress) emailAddress;
@property (T@"NSArray",R,V_contactIdentifiers) contactIdentifiers;
```

## Class methods

```
+[CAMLibrarySelectionIdentity identityWithDevice:];
+[CAMLibrarySelectionIdentity identityWithPerson:];
+[CAMLibrarySelectionIdentity identityWithPhotosIdentity:];
```

## Instance methods

```
-[CAMLibrarySelectionIdentity phoneNumber];
-[CAMLibrarySelectionIdentity emailAddress];
-[CAMLibrarySelectionIdentity hash];
-[CAMLibrarySelectionIdentity description];
-[CAMLibrarySelectionIdentity contactIdentifiers];
-[CAMLibrarySelectionIdentity copyWithZone:];
-[CAMLibrarySelectionIdentity isEqual:];
-[CAMLibrarySelectionIdentity initWithPhoneNumber:emailAddress:contactIdentifiers:];
```
