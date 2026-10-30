# `SRMediaEvent`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `SRSampling`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 6 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"NSString" _mediaIdentifier;
q _eventType;
```

## Properties

```
@property (Tq,N,V_eventType) eventType;
@property (T@"NSString",&,N,V_mediaIdentifier) mediaIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRMediaEvent supportsSecureCoding];
+[SRMediaEvent initialize];
```

## Instance methods

```
-[SRMediaEvent eventType];
-[SRMediaEvent setEventType:];
-[SRMediaEvent dealloc];
-[SRMediaEvent encodeWithCoder:];
-[SRMediaEvent hash];
-[SRMediaEvent description];
-[SRMediaEvent initWithCoder:];
-[SRMediaEvent copyWithZone:];
-[SRMediaEvent isEqual:];
-[SRMediaEvent mediaIdentifier];
-[SRMediaEvent setMediaIdentifier:];
-[SRMediaEvent binarySampleRepresentation];
-[SRMediaEvent initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRMediaEvent sr_dictionaryRepresentation];
-[SRMediaEvent initWithMediaIdentifier:eventType:];
```
