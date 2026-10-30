# `NSHost`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 9 instance methods, 6 class methods

## Instance variables

```
@"NSArray" names;
@"NSArray" addresses;
@ reserved;
```

## Properties

```
@property (T@"NSString",R,C) name;
@property (T@"NSArray",R,C) names;
@property (T@"NSString",R,C) address;
@property (T@"NSArray",R,C) addresses;
@property (T@"NSString",R,C) localizedName;
```

## Class methods

```
+[NSHost currentHost];
+[NSHost flushHostCache];
+[NSHost hostWithAddress:];
+[NSHost hostWithName:];
+[NSHost isHostCacheEnabled];
+[NSHost setHostCacheEnabled:];
```

## Instance methods

```
-[NSHost names];
-[NSHost address];
-[NSHost dealloc];
-[NSHost addresses];
-[NSHost localizedName];
-[NSHost description];
-[NSHost name];
-[NSHost _thingToResolve];
-[NSHost isEqualToHost:];
```
