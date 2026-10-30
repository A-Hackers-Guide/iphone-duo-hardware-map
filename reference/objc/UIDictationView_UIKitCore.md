# `UIDictationView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SUICFlamesViewDelegate`
- 10 instance variables, 7 properties, 29 instance methods, 5 class methods

## Instance variables

```
@"UIKeyboardDicationBackground" _background;
@"UIButton" _endpointButton;
@"UIButton" _endpointButtonLandscape;
i _state;
B _keyboardInTransition;
B _automaticAppearanceWasEnabled;
@"SUICFlamesView" _flamesView;
B _showLanguageLabel;
B _switchingLanguage;
@"<UIDictationViewDisplayDelegate>" _displayDelegate;
```

## Properties

```
@property (TB,N,V_showLanguageLabel) showLanguageLabel;
@property (TB,N,V_switchingLanguage) switchingLanguage;
@property (T@"<UIDictationViewDisplayDelegate>",N,V_displayDelegate) displayDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDictationView sharedInstance];
+[UIDictationView layoutSize];
+[UIDictationView dictationViewClass];
+[UIDictationView viewSize];
+[UIDictationView activeInstance];
```

## Instance methods

```
-[UIDictationView visible];
-[UIDictationView setState:];
-[UIDictationView contentOffset];
-[UIDictationView dealloc];
-[UIDictationView show];
-[UIDictationView applicationWillResignActive];
-[UIDictationView initWithFrame:];
-[UIDictationView displayDelegate];
-[UIDictationView positionForShow];
-[UIDictationView applicationEnteredBackground];
-[UIDictationView audioLevelForFlamesView:];
-[UIDictationView backgroundOffset];
-[UIDictationView currentScreenSize];
-[UIDictationView drawsOwnBackground];
-[UIDictationView endpointButton];
-[UIDictationView endpointButtonPressed];
-[UIDictationView finishReturnToKeyboard];
-[UIDictationView globeButtonPressed:withEvent:location:];
-[UIDictationView highlightEndpointButton];
-[UIDictationView isShowing];
-[UIDictationView keyboardDidShow:];
-[UIDictationView prepareForReturnToKeyboard];
-[UIDictationView removeBackgroundView];
-[UIDictationView returnToKeyboard];
-[UIDictationView setDisplayDelegate:];
-[UIDictationView setShowLanguageLabel:];
-[UIDictationView setSwitchingLanguage:];
-[UIDictationView showLanguageLabel];
-[UIDictationView switchingLanguage];
```
