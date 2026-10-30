# `CAFEntity` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BSInvalidatable`
- 0 instance variables, 6 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"NSUUID",R,N) uniqueIdentifier;
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) typeName;
@property (TB,R,N) usable;
@property (T#,R,N) baseCAFClass;
@property (T@"NSArray",R,N) comparisonKeys;
```

## Instance methods

```
-[CAFEntity typeName];
-[CAFEntity uniqueIdentifier];
-[CAFEntity valueForKeyPath:];
-[CAFEntity name];
-[CAFEntity usable];
-[CAFEntity baseCAFClass];
-[CAFEntity comparisonKeys];
```
