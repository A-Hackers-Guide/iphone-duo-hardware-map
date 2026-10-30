# `SBAppSwitcherService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
@"NSString" _viewServiceClassName;
```

## Properties

```
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",C,N,V_viewServiceClassName) viewServiceClassName;
```

## Class methods

```
+[SBAppSwitcherService switcherServiceWithName:viewServiceClassName:];
```

## Instance methods

```
-[SBAppSwitcherService bundleIdentifier];
-[SBAppSwitcherService setBundleIdentifier:];
-[SBAppSwitcherService setViewServiceClassName:];
-[SBAppSwitcherService viewServiceClassName];
```
