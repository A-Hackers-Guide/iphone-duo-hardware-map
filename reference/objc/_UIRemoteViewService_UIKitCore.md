# `_UIRemoteViewService`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 10 properties, 8 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",R,D,N) identifier;
@property (T@"NSString",R,D,N) xpcServiceNameRoot;
@property (TB,R,D,N) overridesHostAppearance;
@property (TB,R,D,N) multipleInstances;
@property (T@"NSUUID",R,D,N) multipleInstanceUUID;
@property (Ti,R,D,N) processIdentifier;
@property (T@"NSString",R,D,N) viewControllerClassName;
@property (T@"NSUUID",R,C,D,N) contextToken;
@property (T@"<PKPlugIn>",R,N) plugin;
@property (T@"NSString",R,N) extensionPointIdentifier;
```

## Class methods

```
+[_UIRemoteViewService allocWithZone:];
```

## Instance methods

```
-[_UIRemoteViewService init];
-[_UIRemoteViewService extensionPointIdentifier];
-[_UIRemoteViewService _init];
-[_UIRemoteViewService initWithExtension:andContextToken:];
-[_UIRemoteViewService plugin];
-[_UIRemoteViewService endUsing:];
-[_UIRemoteViewService beginUsing:];
-[_UIRemoteViewService initWithPlugIn:andContextToken:];
```
