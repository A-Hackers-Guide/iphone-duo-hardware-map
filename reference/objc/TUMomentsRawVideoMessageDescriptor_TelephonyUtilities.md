# `TUMomentsRawVideoMessageDescriptor`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _uuid;
@"TUSandboxExtendedURL" _videoURL;
```

## Properties

```
@property (T@"NSUUID",R,&,N,V_uuid) uuid;
@property (T@"TUSandboxExtendedURL",R,&,N,V_videoURL) videoURL;
```

## Class methods

```
+[TUMomentsRawVideoMessageDescriptor supportsSecureCoding];
```

## Instance methods

```
-[TUMomentsRawVideoMessageDescriptor uuid];
-[TUMomentsRawVideoMessageDescriptor encodeWithCoder:];
-[TUMomentsRawVideoMessageDescriptor videoURL];
-[TUMomentsRawVideoMessageDescriptor initWithCoder:];
-[TUMomentsRawVideoMessageDescriptor initWithUUID:videoURL:];
```
