# `_UIStatusBarTimeItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarItem`
- 4 instance variables, 4 properties, 15 instance methods, 4 class methods

## Instance variables

```
@"_UIStatusBarStringView" _timeView;
@"_UIStatusBarStringView" _shortTimeView;
@"_UIStatusBarStringView" _pillTimeView;
@"_UIStatusBarStringView" _dateView;
```

## Properties

```
@property (T@"_UIStatusBarStringView",&,N,V_timeView) timeView;
@property (T@"_UIStatusBarStringView",&,N,V_shortTimeView) shortTimeView;
@property (T@"_UIStatusBarStringView",&,N,V_pillTimeView) pillTimeView;
@property (T@"_UIStatusBarStringView",&,N,V_dateView) dateView;
```

## Class methods

```
+[_UIStatusBarTimeItem dateDisplayIdentifier];
+[_UIStatusBarTimeItem pillTimeDisplayIdentifier];
+[_UIStatusBarTimeItem shortTimeDisplayIdentifier];
+[_UIStatusBarTimeItem timeDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarTimeItem setDateView:];
-[_UIStatusBarTimeItem _create_shortTimeView];
-[_UIStatusBarTimeItem dateView];
-[_UIStatusBarTimeItem setTimeView:];
-[_UIStatusBarTimeItem timeView];
-[_UIStatusBarTimeItem viewForIdentifier:];
-[_UIStatusBarTimeItem _create_timeView];
-[_UIStatusBarTimeItem _create_pillTimeView];
-[_UIStatusBarTimeItem dependentEntryKeys];
-[_UIStatusBarTimeItem setPillTimeView:];
-[_UIStatusBarTimeItem applyUpdate:toDisplayItem:];
-[_UIStatusBarTimeItem pillTimeView];
-[_UIStatusBarTimeItem shortTimeView];
-[_UIStatusBarTimeItem _create_dateView];
-[_UIStatusBarTimeItem setShortTimeView:];
```
