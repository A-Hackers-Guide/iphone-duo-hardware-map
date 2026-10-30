# `UIFocusRingClientState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<UIFocusItem>" _currentFocusItem;
@"NSMutableArray" _activeFocusLayers;
@"NSMapTable" _activeFocusLayersToItems;
@"NSString" _clientID;
```

## Properties

```
@property (T@"<UIFocusItem>",W,N,V_currentFocusItem) currentFocusItem;
@property (T@"NSMutableArray",&,N,V_activeFocusLayers) activeFocusLayers;
@property (T@"NSMapTable",&,N,V_activeFocusLayersToItems) activeFocusLayersToItems;
@property (T@"NSString",&,N,V_clientID) clientID;
```

## Instance methods

```
-[UIFocusRingClientState clientID];
-[UIFocusRingClientState setClientID:];
-[UIFocusRingClientState initWithClientID:];
-[UIFocusRingClientState description];
-[UIFocusRingClientState activeFocusLayers];
-[UIFocusRingClientState activeFocusLayersToItems];
-[UIFocusRingClientState currentFocusItem];
-[UIFocusRingClientState setActiveFocusLayers:];
-[UIFocusRingClientState setActiveFocusLayersToItems:];
-[UIFocusRingClientState setCurrentFocusItem:];
```
