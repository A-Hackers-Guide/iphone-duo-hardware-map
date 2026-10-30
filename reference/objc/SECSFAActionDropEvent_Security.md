# `SECSFAActionDropEvent`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _excludeCount;
B _excludeEvent;
{?="excludeCount"b1"excludeEvent"b1} _has;
```

## Properties

```
@property (TB,N) hasExcludeEvent;
@property (TB,N,V_excludeEvent) excludeEvent;
@property (TB,N) hasExcludeCount;
@property (TB,N,V_excludeCount) excludeCount;
```

## Instance methods

```
-[SECSFAActionDropEvent writeTo:];
-[SECSFAActionDropEvent mergeFrom:];
-[SECSFAActionDropEvent hash];
-[SECSFAActionDropEvent copyTo:];
-[SECSFAActionDropEvent description];
-[SECSFAActionDropEvent readFrom:];
-[SECSFAActionDropEvent copyWithZone:];
-[SECSFAActionDropEvent isEqual:];
-[SECSFAActionDropEvent dictionaryRepresentation];
-[SECSFAActionDropEvent hasExcludeEvent];
-[SECSFAActionDropEvent hasExcludeCount];
-[SECSFAActionDropEvent excludeCount];
-[SECSFAActionDropEvent excludeEvent];
-[SECSFAActionDropEvent setExcludeCount:];
-[SECSFAActionDropEvent setExcludeEvent:];
-[SECSFAActionDropEvent setHasExcludeCount:];
-[SECSFAActionDropEvent setHasExcludeEvent:];
```
