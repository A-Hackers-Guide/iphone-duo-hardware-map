# `CWFChannel`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 14 properties, 24 instance methods, 2 class methods

## Instance variables

```
I _flags;
Q _channel;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_channel) channel;
@property (TI,N,V_flags) flags;
@property (Ti,R,D,N) width;
@property (TI,R,N) band;
@property (TB,R,D,N) is2GHz;
@property (TB,R,D,N) is5GHz;
@property (TB,R,D,N) is6GHz;
@property (TB,R,D,N) is6GHzPSC;
@property (TB,R,D,N) overlapsWithUWB;
@property (TB,R,D,N) isDFS;
```

## Class methods

```
+[CWFChannel supportsSecureCoding];
+[CWFChannel channelWithNumber:band:width:];
```

## Instance methods

```
-[CWFChannel setChannel:];
-[CWFChannel channel];
-[CWFChannel JSONCompatibleKeyValueMap];
-[CWFChannel isDFS];
-[CWFChannel debugDescription];
-[CWFChannel setFlags:];
-[CWFChannel flags];
-[CWFChannel externalForm];
-[CWFChannel is6GHzPSC];
-[CWFChannel is6GHz];
-[CWFChannel band];
-[CWFChannel is2GHz];
-[CWFChannel overlapsWithUWB];
-[CWFChannel extAbove];
-[CWFChannel initWithExternalForm:];
-[CWFChannel encodeWithCoder:];
-[CWFChannel isEqualToChannel:];
-[CWFChannel hash];
-[CWFChannel description];
-[CWFChannel initWithCoder:];
-[CWFChannel width];
-[CWFChannel copyWithZone:];
-[CWFChannel isEqual:];
-[CWFChannel is5GHz];
```
