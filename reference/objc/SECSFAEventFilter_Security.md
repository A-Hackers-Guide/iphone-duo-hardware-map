# `SECSFAEventFilter`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
q _dropRate;
@"NSString" _event;
{?="dropRate"b1} _has;
```

## Properties

```
@property (TB,R,N) hasEvent;
@property (T@"NSString",&,N,V_event) event;
@property (TB,N) hasDropRate;
@property (Tq,N,V_dropRate) dropRate;
```

## Instance methods

```
-[SECSFAEventFilter setEvent:];
-[SECSFAEventFilter writeTo:];
-[SECSFAEventFilter mergeFrom:];
-[SECSFAEventFilter event];
-[SECSFAEventFilter hash];
-[SECSFAEventFilter copyTo:];
-[SECSFAEventFilter description];
-[SECSFAEventFilter readFrom:];
-[SECSFAEventFilter copyWithZone:];
-[SECSFAEventFilter isEqual:];
-[SECSFAEventFilter dictionaryRepresentation];
-[SECSFAEventFilter setHasDropRate:];
-[SECSFAEventFilter dropRate];
-[SECSFAEventFilter hasDropRate];
-[SECSFAEventFilter hasEvent];
-[SECSFAEventFilter setDropRate:];
```
