# `BKMatchEvent`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
B _result;
Q _timeStamp;
@"BKIdentity" _matchedIdentity;
```

## Properties

```
@property (TB,N,V_result) result;
@property (TQ,N,V_timeStamp) timeStamp;
@property (T@"BKIdentity",&,N,V_matchedIdentity) matchedIdentity;
```

## Class methods

```
+[BKMatchEvent matchEventWithDictionary:device:error:];
```

## Instance methods

```
-[BKMatchEvent setResult:];
-[BKMatchEvent result];
-[BKMatchEvent setTimeStamp:];
-[BKMatchEvent timeStamp];
-[BKMatchEvent matchedIdentity];
-[BKMatchEvent setMatchedIdentity:];
```
