# `CTAppleAccountDsids`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSString" _iCloudDsid;
@"NSString" _iMessageDsid;
@"NSString" _faceTimeDsid;
```

## Properties

```
@property (T@"NSString",R,V_iCloudDsid) iCloudDsid;
@property (T@"NSString",R,V_iMessageDsid) iMessageDsid;
@property (T@"NSString",R,V_faceTimeDsid) faceTimeDsid;
```

## Class methods

```
+[CTAppleAccountDsids supportsSecureCoding];
```

## Instance methods

```
-[CTAppleAccountDsids encodeWithCoder:];
-[CTAppleAccountDsids hash];
-[CTAppleAccountDsids description];
-[CTAppleAccountDsids initWithCoder:];
-[CTAppleAccountDsids copyWithZone:];
-[CTAppleAccountDsids isEqual:];
-[CTAppleAccountDsids areMessageFaceTimeSetup];
-[CTAppleAccountDsids doDsidsMatch];
-[CTAppleAccountDsids faceTimeDsid];
-[CTAppleAccountDsids iCloudDsid];
-[CTAppleAccountDsids iMessageDsid];
-[CTAppleAccountDsids initWithICloudDsid:iMessageDsid:faceTimeDsid:];
```
