# `_UIFeedbackVisualizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _feedbackWindows;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_feedbackWindows) feedbackWindows;
```

## Class methods

```
+[_UIFeedbackVisualizer sharedVisualizer];
```

## Instance methods

```
-[_UIFeedbackVisualizer observeValueForKeyPath:ofObject:change:context:];
-[_UIFeedbackVisualizer init];
-[_UIFeedbackVisualizer feedbackWindows];
-[_UIFeedbackVisualizer _colorForEngine:];
-[_UIFeedbackVisualizer _colorForEngineState:];
-[_UIFeedbackVisualizer _colorForFeedback:];
-[_UIFeedbackVisualizer _monogramForEngine:];
-[_UIFeedbackVisualizer _showVisualForFeedback:];
-[_UIFeedbackVisualizer _updateEngine:];
-[_UIFeedbackVisualizer addEngine:];
-[_UIFeedbackVisualizer cancelVisualForFeedback:];
-[_UIFeedbackVisualizer engineLayersForEngine:];
-[_UIFeedbackVisualizer setFeedbackWindows:];
-[_UIFeedbackVisualizer showVisualForFeedback:withDelay:];
-[_UIFeedbackVisualizer visualFeedbackWindowForScene:];
```
