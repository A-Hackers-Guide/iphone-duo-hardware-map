# `PKTextEffectsWindowObserver`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedKeyWindowBounds;
q _cachedKeyWindowUIStyle;
@"<PKTextEffectsWindowObserverDelegate>" _delegate;
@"UITextEffectsWindow" _textEffectsWindow;
```

## Instance methods

```
-[PKTextEffectsWindowObserver observeValueForKeyPath:ofObject:change:context:];
-[PKTextEffectsWindowObserver dealloc];
-[PKTextEffectsWindowObserver _handleKeyWindowDidChangeNotification:];
-[PKTextEffectsWindowObserver _handleSceneDidActivateNotification:];
-[PKTextEffectsWindowObserver _handleTextEffectsWindowDidRotateNotification:];
```
