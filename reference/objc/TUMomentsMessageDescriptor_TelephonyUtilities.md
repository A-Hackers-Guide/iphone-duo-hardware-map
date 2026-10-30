# `TUMomentsMessageDescriptor`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _messageUUID;
@"TUSandboxExtendedURL" _videoURL;
@"TUSandboxExtendedURL" _thumbnailURL;
```

## Properties

```
@property (T@"NSUUID",R,N,V_messageUUID) messageUUID;
@property (T@"TUSandboxExtendedURL",R,N,V_videoURL) videoURL;
@property (T@"TUSandboxExtendedURL",R,N,V_thumbnailURL) thumbnailURL;
```

## Class methods

```
+[TUMomentsMessageDescriptor supportsSecureCoding];
```

## Instance methods

```
-[TUMomentsMessageDescriptor messageUUID];
-[TUMomentsMessageDescriptor encodeWithCoder:];
-[TUMomentsMessageDescriptor videoURL];
-[TUMomentsMessageDescriptor initWithCoder:];
-[TUMomentsMessageDescriptor thumbnailURL];
-[TUMomentsMessageDescriptor initWithMessageUUID:videoURL:thumbnailURL:];
```
