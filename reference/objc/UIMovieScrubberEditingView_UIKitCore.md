# `UIMovieScrubberEditingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _leftImageView;
@"UIImageView" _middleImageView;
@"UIImageView" _rightImageView;
@"NSArray" _activeImages;
@"NSArray" _activeNoEditImages;
@"NSArray" _inactiveImages;
B _enabled;
B _editing;
d _edgeInset;
```

## Properties

```
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N,GisEditing,V_editing) editing;
@property (Td,N,V_edgeInset) edgeInset;
```

## Instance methods

```
-[UIMovieScrubberEditingView layoutSubviews];
-[UIMovieScrubberEditingView isEnabled];
-[UIMovieScrubberEditingView setEditing:];
-[UIMovieScrubberEditingView setEnabled:];
-[UIMovieScrubberEditingView isEditing];
-[UIMovieScrubberEditingView initWithFrame:];
-[UIMovieScrubberEditingView bounce];
-[UIMovieScrubberEditingView _leftHandleRect];
-[UIMovieScrubberEditingView _bounceValueForFraction:];
-[UIMovieScrubberEditingView _handleImages];
-[UIMovieScrubberEditingView _rightHandleRect];
-[UIMovieScrubberEditingView _updateHandleImages];
-[UIMovieScrubberEditingView edgeInset];
-[UIMovieScrubberEditingView handleForPoint:hitOffset:];
-[UIMovieScrubberEditingView pointInsideLeftHandle:];
-[UIMovieScrubberEditingView pointInsideRightHandle:];
-[UIMovieScrubberEditingView setEdgeInset:];
```
