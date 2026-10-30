# `CAFControlParameter`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`
- 4 instance variables, 9 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _supportsInvalid;
@"NSString" _name;
Q _format;
@"CAFCachedDescription" _cachedDescription;
```

## Properties

```
@property (T@"CAFCachedDescription",&,N,V_cachedDescription) cachedDescription;
@property (T@"NSString",R,N,V_name) name;
@property (TQ,R,N,V_format) format;
@property (T@"NSString",R,N) formatString;
@property (TB,R,N,V_supportsInvalid) supportsInvalid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFControlParameter parseParameters:];
```

## Instance methods

```
-[CAFControlParameter cachedDescription];
-[CAFControlParameter formatString];
-[CAFControlParameter initWithConfig:];
-[CAFControlParameter setCachedDescription:];
-[CAFControlParameter format];
-[CAFControlParameter name];
-[CAFControlParameter supportsInvalid];
-[CAFControlParameter currentDescriptionForCache:];
```
