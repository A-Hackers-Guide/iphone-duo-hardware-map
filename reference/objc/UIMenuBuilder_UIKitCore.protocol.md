# `UIMenuBuilder` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 1 properties, 24 instance methods, 0 class methods

## Properties

```
@property (T@"UIMenuSystem",R,N) system;
```

## Instance methods

```
-[UIMenuBuilder insertElements:afterActionForIdentifier:];
-[UIMenuBuilder removeCommandForAction:propertyList:];
-[UIMenuBuilder insertElements:beforeActionForIdentifier:];
-[UIMenuBuilder insertChildMenu:atStartOfMenuForIdentifier:];
-[UIMenuBuilder replaceCommandForAction:propertyList:withElements:];
-[UIMenuBuilder commandForAction:propertyList:];
-[UIMenuBuilder insertElements:atStartOfMenuForIdentifier:];
-[UIMenuBuilder replaceChildrenOfMenuForIdentifier:fromChildrenBlock:];
-[UIMenuBuilder menuForIdentifier:];
-[UIMenuBuilder insertElements:afterMenuForIdentifier:];
-[UIMenuBuilder insertSiblingMenu:beforeMenuForIdentifier:];
-[UIMenuBuilder insertChildMenu:atEndOfMenuForIdentifier:];
-[UIMenuBuilder insertElements:beforeCommandForAction:propertyList:];
-[UIMenuBuilder replaceMenuForIdentifier:withElements:];
-[UIMenuBuilder insertElements:atEndOfMenuForIdentifier:];
-[UIMenuBuilder replaceActionForIdentifier:withElements:];
-[UIMenuBuilder insertSiblingMenu:afterMenuForIdentifier:];
-[UIMenuBuilder removeMenuForIdentifier:];
-[UIMenuBuilder insertElements:afterCommandForAction:propertyList:];
-[UIMenuBuilder replaceMenuForIdentifier:withMenu:];
-[UIMenuBuilder actionForIdentifier:];
-[UIMenuBuilder insertElements:beforeMenuForIdentifier:];
-[UIMenuBuilder removeActionForIdentifier:];
-[UIMenuBuilder system];
```
