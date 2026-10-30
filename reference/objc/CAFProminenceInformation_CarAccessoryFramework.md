# `CAFProminenceInformation`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
C _color;
C _sortOrder;
Q _prominenceLevel;
@"NSString" _userVisibleLabel;
@"NSString" _userVisibleValue;
```

## Properties

```
@property (TC,R,N,V_color) color;
@property (TQ,R,N,V_prominenceLevel) prominenceLevel;
@property (TC,R,N,V_sortOrder) sortOrder;
@property (T@"NSString",R,C,N,V_userVisibleLabel) userVisibleLabel;
@property (T@"NSString",R,C,N,V_userVisibleValue) userVisibleValue;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
```

## Instance methods

```
-[CAFProminenceInformation sortOrder];
-[CAFProminenceInformation initWithDictionary:];
-[CAFProminenceInformation color];
-[CAFProminenceInformation description];
-[CAFProminenceInformation dictionaryRepresentation];
-[CAFProminenceInformation userVisibleLabel];
-[CAFProminenceInformation userVisibleValue];
-[CAFProminenceInformation prominenceLevel];
-[CAFProminenceInformation initWithColor:prominenceLevel:sortOrder:userVisibleLabel:userVisibleValue:];
```
