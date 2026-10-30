# `TPMessageIndicatorViewModel`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 12 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isRead;
B _isVideo;
d _duration;
@"NSString" _identifier;
@"NSURL" _mediaURL;
@"NSURL" _thumbnailURL;
@"NSString" _transcriptSummary;
@"TUHandle" _fromHandle;
@"SCSensitivityAnalysis" _sensitivityAnalysis;
```

## Properties

```
@property (Td,R,N,V_duration) duration;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSURL",R,N,V_mediaURL) mediaURL;
@property (T@"NSURL",R,N,V_thumbnailURL) thumbnailURL;
@property (T@"NSString",R,N,V_transcriptSummary) transcriptSummary;
@property (TB,R,N,V_isRead) isRead;
@property (TB,R,N) isSensitive;
@property (TB,R,N,V_isVideo) isVideo;
@property (T@"TUHandle",R,N,V_fromHandle) fromHandle;
@property (T{CGSize=dd},R,N) indicatorImageSize;
@property (T@"SCSensitivityAnalysis",R,N,V_sensitivityAnalysis) sensitivityAnalysis;
@property (T@"NSUUID",R,N) messageUUID;
```

## Instance methods

```
-[TPMessageIndicatorViewModel messageUUID];
-[TPMessageIndicatorViewModel mediaURL];
-[TPMessageIndicatorViewModel fromHandle];
-[TPMessageIndicatorViewModel identifier];
-[TPMessageIndicatorViewModel init];
-[TPMessageIndicatorViewModel isRead];
-[TPMessageIndicatorViewModel duration];
-[TPMessageIndicatorViewModel isSensitive];
-[TPMessageIndicatorViewModel description];
-[TPMessageIndicatorViewModel thumbnailURL];
-[TPMessageIndicatorViewModel copyWithZone:];
-[TPMessageIndicatorViewModel isVideo];
-[TPMessageIndicatorViewModel initWithIdentifier:];
-[TPMessageIndicatorViewModel sensitivityAnalysis];
-[TPMessageIndicatorViewModel indicatorImageSize];
-[TPMessageIndicatorViewModel indicatorImageWithDefaultTintColor:];
-[TPMessageIndicatorViewModel initWithDuration:identifier:mediaURL:thumbnailURL:transcriptSummary:isRead:sensitivityAnalysis:isVideo:fromHandle:];
-[TPMessageIndicatorViewModel transcriptSummary];
```
