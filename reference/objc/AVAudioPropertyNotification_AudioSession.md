# `AVAudioPropertyNotification`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _propertyName;
@"NSNumber" _sourceSessionID;
@"NSNumber" _nodeSessionID;
@"NSDictionary" _propertyData;
```

## Properties

```
@property (T@"NSString",R,N,V_propertyName) propertyName;
@property (T@"NSNumber",R,N,V_sourceSessionID) sourceSessionID;
@property (T@"NSNumber",R,N,V_nodeSessionID) nodeSessionID;
@property (T@"NSDictionary",R,N,V_propertyData) propertyData;
```

## Instance methods

```
-[AVAudioPropertyNotification propertyName];
-[AVAudioPropertyNotification sourceSessionID];
-[AVAudioPropertyNotification propertyData];
-[AVAudioPropertyNotification initWithInternal:];
-[AVAudioPropertyNotification nodeSessionID];
```
