# `BTCloudSoundProfileRecord`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSData" _soundProfileData;
@"NSURL" _soundProfileFileURL;
```

## Properties

```
@property (T@"NSData",&,N,V_soundProfileData) soundProfileData;
@property (T@"NSURL",&,N,V_soundProfileFileURL) soundProfileFileURL;
```

## Class methods

```
+[BTCloudSoundProfileRecord supportsSecureCoding];
+[BTCloudSoundProfileRecord soundProfileRecordWithCustomData:];
+[BTCloudSoundProfileRecord soundProfileRecordWithFileURL:];
```

## Instance methods

```
-[BTCloudSoundProfileRecord initWithFileURL:];
-[BTCloudSoundProfileRecord encodeWithCoder:];
-[BTCloudSoundProfileRecord description];
-[BTCloudSoundProfileRecord initWithCoder:];
-[BTCloudSoundProfileRecord soundProfileData];
-[BTCloudSoundProfileRecord initWithCustomData:];
-[BTCloudSoundProfileRecord setSoundProfileData:];
-[BTCloudSoundProfileRecord setSoundProfileFileURL:];
-[BTCloudSoundProfileRecord soundProfileFileURL];
```
