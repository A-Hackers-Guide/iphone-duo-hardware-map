# `UISwitchDesignLibraryVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISwitchVisualElement`
- Protocols: `UISwitchMVEGestureTrackingSessionElement`, `UIGestureRecognizerDelegate`
- 11 instance variables, 1 properties, 24 instance methods, 2 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isOn;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isPressed;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 tapSeed;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 customizations;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 coreHostingView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 gestureTrackingSession;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 longPressGestureRecognizer;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 panGestureRecognizer;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 tapGestureRecognizer;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 selectGestureRecognizer;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 feedbackGenerator;
```

## Properties

```
@property (T@"<UISwitchControl>",N,&) switchControl;
```

## Class methods

```
+[UISwitchDesignLibraryVisualElement preferredContentSize];
+[UISwitchDesignLibraryVisualElement isFixedSize];
```

## Instance methods

```
-[UISwitchDesignLibraryVisualElement displayedOn];
-[UISwitchDesignLibraryVisualElement setOnTintColor:];
-[UISwitchDesignLibraryVisualElement gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[UISwitchDesignLibraryVisualElement setOnImage:];
-[UISwitchDesignLibraryVisualElement init];
-[UISwitchDesignLibraryVisualElement gestureRecognizer:shouldReceiveEvent:];
-[UISwitchDesignLibraryVisualElement layoutSubviews];
-[UISwitchDesignLibraryVisualElement setOn:animated:];
-[UISwitchDesignLibraryVisualElement handleLongPress:];
-[UISwitchDesignLibraryVisualElement handlePan:];
-[UISwitchDesignLibraryVisualElement handleTap:];
-[UISwitchDesignLibraryVisualElement gestureRecognizerShouldBegin:];
-[UISwitchDesignLibraryVisualElement setTintColor:];
-[UISwitchDesignLibraryVisualElement setShowsOnOffLabel:];
-[UISwitchDesignLibraryVisualElement setOffImage:];
-[UISwitchDesignLibraryVisualElement gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UISwitchDesignLibraryVisualElement initWithCoder:];
-[UISwitchDesignLibraryVisualElement sendStateChangeActions];
-[UISwitchDesignLibraryVisualElement setThumbTintColor:];
-[UISwitchDesignLibraryVisualElement setSwitchControl:];
-[UISwitchDesignLibraryVisualElement initWithFrame:];
-[UISwitchDesignLibraryVisualElement interactiveChangeToDisplayedOn:];
-[UISwitchDesignLibraryVisualElement selectGestureChanged:];
-[UISwitchDesignLibraryVisualElement switchControl];
```
