# `UIKBScreenTraits`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 32 instance variables, 31 properties, 55 instance methods, 13 class methods

## Instance variables

```
B _isEmulatingIdiom;
q _idiomToEmulate;
B _knobInput;
B _touchInput;
B _touchpadInput;
B _isKeyboardMinorEdgeWidth;
B _isInPopover;
B _isSplit;
B _supportsSplit;
B _centerFilled;
B _isFloating;
B _isLinear;
B _prefersCompactNumberPadLayout;
B _resizeKeyboardHeight;
B _isFirstPartyStickers;
B _isEmojiPosterOniPad;
B _isPINSetupController;
B _isStickerPickerService;
B _isStickerPickerServiceCollectionView;
@"UIScreen" _screen;
q _orientation;
d _keyboardWidth;
d _keyboardBarHeight;
q _preferredEmojiScrollingDirection;
d _assistantViewWidth;
d _keyboardHeightAdjustment;
d _hostKeyboardWidth;
d _screenToNativeScaleRatio;
{CGSize="width"d"height"d} _stretchFactor;
{CGSize="width"d"height"d} _preferredContentSizeInPopover;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _assistantViewWindowBounds;
```

## Properties

```
@property (Tq,N,V_preferredEmojiScrollingDirection) preferredEmojiScrollingDirection;
@property (T@"UIScreen",R,N,V_screen) screen;
@property (Tq,R,N) idiom;
@property (TB,R,N,V_knobInput) knobInput;
@property (TB,R,N,V_touchInput) touchInput;
@property (TB,R,N,V_touchpadInput) touchpadInput;
@property (Tq,N,V_orientation) orientation;
@property (Tq,R,N) horizontalSizeClass;
@property (Tq,R,N) verticalSizeClass;
@property (Td,N,V_keyboardWidth) keyboardWidth;
@property (Td,N,V_assistantViewWidth) assistantViewWidth;
@property (Td,R,N) reachableKeyboardDefinedWidth;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_bounds) bounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_assistantViewWindowBounds) assistantViewWindowBounds;
@property (TB,R,N,V_isKeyboardMinorEdgeWidth) isKeyboardMinorEdgeWidth;
@property (Td,N,V_keyboardBarHeight) keyboardBarHeight;
@property (TB,R,N,V_isInPopover) isInPopover;
@property (TB,R,N,V_isFloating) isFloating;
@property (TB,R,N) isEmulatingIdiom;
@property (TB,N,V_isSplit) isSplit;
@property (TB,N,V_supportsSplit) supportsSplit;
@property (TB,N,V_centerFilled) centerFilled;
@property (T{CGSize=dd},R,N) keyboardScreenReferenceSize;
@property (T{CGSize=dd},N,V_stretchFactor) stretchFactor;
@property (TB,R,N,V_isLinear) isLinear;
@property (TB,R,N,V_prefersCompactNumberPadLayout) prefersCompactNumberPadLayout;
@property (TB,R,N) isEmojiScrollingDirectionVertical;
@property (TB,N,V_resizeKeyboardHeight) resizeKeyboardHeight;
@property (Td,N,V_keyboardHeightAdjustment) keyboardHeightAdjustment;
@property (Td,N,V_screenToNativeScaleRatio) screenToNativeScaleRatio;
@property (T{CGSize=dd},N,V_preferredContentSizeInPopover) preferredContentSizeInPopover;
```

## Class methods

```
+[UIKBScreenTraits traitsForPopoverEmulatingWidth:minorEdge:orientation:idiom:];
+[UIKBScreenTraits _orientationReconciledWithGeometry:windowOrientation:reportedOrientation:];
+[UIKBScreenTraits traitsWithScreen:orientation:ignoreRemoteKeyboard:];
+[UIKBScreenTraits _activeUCBWindowForScreen:];
+[UIKBScreenTraits setMockIdiom:];
+[UIKBScreenTraits fullScreenTraitsWithScreen:orientation:];
+[UIKBScreenTraits traitsForInputModeWithScreen:];
+[UIKBScreenTraits traitsWithScreen:orientation:];
+[UIKBScreenTraits keyboardTraitsForWindowScene:];
+[UIKBScreenTraits traitsForRemoteEmojiKeyboardForHostWidth:clientWidth:minorEdge:orientation:idiom:isPopover:];
+[UIKBScreenTraits _windowGeometryDescribesScreenOrientation:screenPortraitSize:];
+[UIKBScreenTraits _activeKeyboardWindowForScreen:];
+[UIKBScreenTraits acceptsSplitKeyboardForTextInputTraits:screenTraits:];
```

## Instance methods

```
-[UIKBScreenTraits isSplit];
-[UIKBScreenTraits setOrientation:];
-[UIKBScreenTraits centerFilled];
-[UIKBScreenTraits supportsSplit];
-[UIKBScreenTraits screen];
-[UIKBScreenTraits isFloating];
-[UIKBScreenTraits verticalSizeClass];
-[UIKBScreenTraits stretchFactor];
-[UIKBScreenTraits knobInput];
-[UIKBScreenTraits keyboardHeightAdjustment];
-[UIKBScreenTraits initWithScreen:orientation:allowFloating:ignoreRemoteKeyboard:];
-[UIKBScreenTraits setCenterFilled:];
-[UIKBScreenTraits touchInput];
-[UIKBScreenTraits assistantViewWindowBounds];
-[UIKBScreenTraits orientation];
-[UIKBScreenTraits setSupportsSplit:];
-[UIKBScreenTraits isEmulatingIdiom];
-[UIKBScreenTraits keyboardScreenReferenceSize];
-[UIKBScreenTraits isInPopover];
-[UIKBScreenTraits keyboardWidth];
-[UIKBScreenTraits defaultLayoutClassForScreenTraits];
-[UIKBScreenTraits keyboardBarHeight];
-[UIKBScreenTraits setBounds:];
-[UIKBScreenTraits setResizeKeyboardHeight:];
-[UIKBScreenTraits initForInputModeWithScreen:];
-[UIKBScreenTraits setPreferredEmojiScrollingDirection:];
-[UIKBScreenTraits preferredEmojiScrollingDirection];
-[UIKBScreenTraits setPreferredContentSizeInPopover:];
-[UIKBScreenTraits setKeyboardWidth:];
-[UIKBScreenTraits traitsSupportPadStyleCandidateBar];
-[UIKBScreenTraits setAssistantViewWindowBounds:];
-[UIKBScreenTraits isLinear];
-[UIKBScreenTraits setKeyboardHeightAdjustment:];
-[UIKBScreenTraits setStretchFactor:];
-[UIKBScreenTraits updateForTextInputTraits:supportedInteractionModel:];
-[UIKBScreenTraits assistantViewWidth];
-[UIKBScreenTraits traitsSupportMode:];
-[UIKBScreenTraits setAssistantViewWidth:];
-[UIKBScreenTraits setKeyboardBarHeight:];
-[UIKBScreenTraits bounds];
-[UIKBScreenTraits screenToNativeScaleRatio];
-[UIKBScreenTraits updateForLinearLayout:];
-[UIKBScreenTraits description];
-[UIKBScreenTraits reachableKeyboardDefinedWidth];
-[UIKBScreenTraits updateForCompactNumberPadLayout:];
-[UIKBScreenTraits touchpadInput];
-[UIKBScreenTraits horizontalSizeClass];
-[UIKBScreenTraits isKeyboardMinorEdgeWidth];
-[UIKBScreenTraits setScreenToNativeScaleRatio:];
-[UIKBScreenTraits resizeKeyboardHeight];
-[UIKBScreenTraits isEmojiScrollingDirectionVertical];
-[UIKBScreenTraits preferredContentSizeInPopover];
-[UIKBScreenTraits setIsSplit:];
-[UIKBScreenTraits prefersCompactNumberPadLayout];
-[UIKBScreenTraits idiom];
```
