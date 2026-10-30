# `AVAudioApplicationSpecification`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__libSessionUtility.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
q audioAppType;
@"NSString" attributionBundleID;
@"NSString" processName;
{?="val"[8I]} _appAuditToken;
```

## Properties

```
@property (Tq,N,VaudioAppType) audioAppType;
@property (T{?=[8I]},N,V_appAuditToken) appAuditToken;
@property (T@"NSString",&,N,VattributionBundleID) attributionBundleID;
@property (T@"NSString",&,N,VprocessName) processName;
```

## Class methods

```
+[AVAudioApplicationSpecification supportsSecureCoding];
```

## Instance methods

```
-[AVAudioApplicationSpecification setProcessName:];
-[AVAudioApplicationSpecification processName];
-[AVAudioApplicationSpecification encodeWithCoder:];
-[AVAudioApplicationSpecification initWithCoder:];
-[AVAudioApplicationSpecification appAuditToken];
-[AVAudioApplicationSpecification audioAppType];
-[AVAudioApplicationSpecification setAppAuditToken:];
-[AVAudioApplicationSpecification setAttributionBundleID:];
-[AVAudioApplicationSpecification setAudioAppType:];
-[AVAudioApplicationSpecification attributionBundleID];
```
