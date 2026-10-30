# `NIAcwgM4Msg`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 10 instance methods, 2 class methods

## Instance variables

```
C _selectedSyncCodeIndex;
I _stsIndex0;
I _hopKey;
Q _uwbTime0;
```

## Properties

```
@property (TI,R,N,V_stsIndex0) stsIndex0;
@property (TQ,R,N,V_uwbTime0) uwbTime0;
@property (TI,R,N,V_hopKey) hopKey;
@property (TC,R,N,V_selectedSyncCodeIndex) selectedSyncCodeIndex;
```

## Class methods

```
+[NIAcwgM4Msg supportsSecureCoding];
+[NIAcwgM4Msg fromStruct:];
```

## Instance methods

```
-[NIAcwgM4Msg encodeWithCoder:];
-[NIAcwgM4Msg description];
-[NIAcwgM4Msg initWithCoder:];
-[NIAcwgM4Msg copyWithZone:];
-[NIAcwgM4Msg hopKey];
-[NIAcwgM4Msg initWithStsIndex0:uwbTime0:hopKey:selectedSyncCodeIndex:];
-[NIAcwgM4Msg selectedSyncCodeIndex];
-[NIAcwgM4Msg stsIndex0];
-[NIAcwgM4Msg toStruct];
-[NIAcwgM4Msg uwbTime0];
```
