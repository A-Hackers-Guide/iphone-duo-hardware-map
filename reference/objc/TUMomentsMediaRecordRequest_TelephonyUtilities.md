# `TUMomentsMediaRecordRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _callUUID;
@"TUSandboxExtendedURL" _sandboxURL;
@"TUMediaTokens" _mediaTokens;
@"NSString" _localeIdentifier;
@"NSString" _localCaptionsFileName;
@"NSString" _remoteCaptionsFileName;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_callUUID) callUUID;
@property (T@"TUSandboxExtendedURL",R,N,V_sandboxURL) sandboxURL;
@property (T@"TUMediaTokens",R,N,V_mediaTokens) mediaTokens;
@property (T@"NSString",C,N,V_localeIdentifier) localeIdentifier;
@property (T@"NSString",C,N,V_localCaptionsFileName) localCaptionsFileName;
@property (T@"NSString",C,N,V_remoteCaptionsFileName) remoteCaptionsFileName;
```

## Class methods

```
+[TUMomentsMediaRecordRequest supportsSecureCoding];
```

## Instance methods

```
-[TUMomentsMediaRecordRequest setLocaleIdentifier:];
-[TUMomentsMediaRecordRequest localeIdentifier];
-[TUMomentsMediaRecordRequest callUUID];
-[TUMomentsMediaRecordRequest encodeWithCoder:];
-[TUMomentsMediaRecordRequest description];
-[TUMomentsMediaRecordRequest initWithCoder:];
-[TUMomentsMediaRecordRequest isEqual:];
-[TUMomentsMediaRecordRequest initWithCall:URL:];
-[TUMomentsMediaRecordRequest initWithCallUUID:URL:mediaTokens:];
-[TUMomentsMediaRecordRequest isEqualToMediaRecordRequest:];
-[TUMomentsMediaRecordRequest localCaptionsFileName];
-[TUMomentsMediaRecordRequest mediaTokens];
-[TUMomentsMediaRecordRequest remoteCaptionsFileName];
-[TUMomentsMediaRecordRequest sandboxURL];
-[TUMomentsMediaRecordRequest setLocalCaptionsFileName:];
-[TUMomentsMediaRecordRequest setRemoteCaptionsFileName:];
```
