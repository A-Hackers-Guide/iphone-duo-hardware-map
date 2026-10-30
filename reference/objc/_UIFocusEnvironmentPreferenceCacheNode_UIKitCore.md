# `_UIFocusEnvironmentPreferenceCacheNode`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _parentNodes;
{?="resolved"b1"resolvedExplicitly"b1} _flags;
@"<UIFocusEnvironment>" _environment;
@"<UIFocusEnvironment>" _resolvedEnvironment;
@"NSArray" _childNodes;
```

## Properties

```
@property (TB,R,N,GisResolved) resolved;
@property (T@"<UIFocusEnvironment>",R,N,V_environment) environment;
@property (T@"<UIFocusEnvironment>",R,N,V_resolvedEnvironment) resolvedEnvironment;
@property (T@"NSArray",C,N,V_childNodes) childNodes;
```

## Instance methods

```
-[_UIFocusEnvironmentPreferenceCacheNode initWithEnvironment:];
-[_UIFocusEnvironmentPreferenceCacheNode debugDescription];
-[_UIFocusEnvironmentPreferenceCacheNode resolve:];
-[_UIFocusEnvironmentPreferenceCacheNode isResolved];
-[_UIFocusEnvironmentPreferenceCacheNode setChildNodes:];
-[_UIFocusEnvironmentPreferenceCacheNode description];
-[_UIFocusEnvironmentPreferenceCacheNode environment];
-[_UIFocusEnvironmentPreferenceCacheNode childNodes];
-[_UIFocusEnvironmentPreferenceCacheNode _reevaluateResolution];
-[_UIFocusEnvironmentPreferenceCacheNode _resolve:explicitly:];
-[_UIFocusEnvironmentPreferenceCacheNode _unresolve];
-[_UIFocusEnvironmentPreferenceCacheNode resolvedEnvironment];
```
