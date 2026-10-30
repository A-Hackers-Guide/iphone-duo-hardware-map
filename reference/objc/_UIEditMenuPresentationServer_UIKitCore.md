# `_UIEditMenuPresentationServer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIEditMenuPresentationDelegate`
- 3 instance variables, 7 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _configurations;
@"NSMutableDictionary" _presentations;
@"NSMutableDictionary" _connections;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_configurations) configurations;
@property (T@"NSMutableDictionary",&,N,V_presentations) presentations;
@property (T@"NSMutableDictionary",&,N,V_connections) connections;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIEditMenuPresentationServer sharedPresentationServer];
```

## Instance methods

```
-[_UIEditMenuPresentationServer _editMenuPresentation:willPresentMenuForConfiguration:animator:];
-[_UIEditMenuPresentationServer setPresentations:];
-[_UIEditMenuPresentationServer presentations];
-[_UIEditMenuPresentationServer connections];
-[_UIEditMenuPresentationServer init];
-[_UIEditMenuPresentationServer _editMenuPresentation:didTransitionMenuForConfiguration:];
-[_UIEditMenuPresentationServer setConnections:];
-[_UIEditMenuPresentationServer configurations];
-[_UIEditMenuPresentationServer _editMenuPresentation:handoffDisplayedMenuWithContext:];
-[_UIEditMenuPresentationServer _editMenuPresentation:preparedMenuForDisplay:completion:];
-[_UIEditMenuPresentationServer _editMenuPresentation:preferredLayoutRectsForConfiguration:];
-[_UIEditMenuPresentationServer _editMenuPresentation:titleViewForMenu:configuration:];
-[_UIEditMenuPresentationServer _editMenuPresentation:willDismissMenuForConfiguration:animator:];
-[_UIEditMenuPresentationServer _editMenuPresentation:targetRectForConfiguration:];
-[_UIEditMenuPresentationServer _editMenuPresentation:didSelectMenuLeaf:completion:];
-[_UIEditMenuPresentationServer setConfigurations:];
-[_UIEditMenuPresentationServer _sendLifecycleEvent:forMenuWithIdentifier:];
-[_UIEditMenuPresentationServer dismissEditMenuForIdentifier:hideReason:];
-[_UIEditMenuPresentationServer presentEditMenuWithConfiguration:originContext:inDisplayDelegate:forConnection:];
-[_UIEditMenuPresentationServer replaceEditMenuForIdentifier:updatedMenu:reason:];
-[_UIEditMenuPresentationServer updateUserInterfaceStyleForMenuWithIdentifier:userInterfaceStyle:];
```
