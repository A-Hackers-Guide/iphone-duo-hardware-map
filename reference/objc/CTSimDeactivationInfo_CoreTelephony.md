# `CTSimDeactivationInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSString" _homePlmn;
@"NSMutableArray" _events;
```

## Properties

```
@property (T@"NSString",&,N,V_homePlmn) homePlmn;
@property (T@"NSMutableArray",&,N,V_events) events;
```

## Class methods

```
+[CTSimDeactivationInfo supportsSecureCoding];
```

## Instance methods

```
-[CTSimDeactivationInfo setEvents:];
-[CTSimDeactivationInfo events];
-[CTSimDeactivationInfo encodeWithCoder:];
-[CTSimDeactivationInfo description];
-[CTSimDeactivationInfo initWithCoder:];
-[CTSimDeactivationInfo isEqual:];
-[CTSimDeactivationInfo homePlmn];
-[CTSimDeactivationInfo setHomePlmn:];
```
