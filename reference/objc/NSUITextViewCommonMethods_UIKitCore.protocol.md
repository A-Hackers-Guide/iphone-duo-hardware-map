# `NSUITextViewCommonMethods` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSTextLayoutOrientationProvider`, `NSTextContainerView`
- 0 instance variables, 4 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSLayoutManager",R,N) layoutManager;
@property (T@"NSTextContainer",?,W,N) textContainer;
@property (T{_NSRange=QQ},?,N) markedRange;
@property (T@"NSDictionary",?,R,N) markedTextStyle;
```

## Instance methods

```
-[NSUITextViewCommonMethods minSize];
-[NSUITextViewCommonMethods visibleRect];
-[NSUITextViewCommonMethods layoutManager];
-[NSUITextViewCommonMethods isHorizontallyResizable];
-[NSUITextViewCommonMethods textContainerOrigin];
-[NSUITextViewCommonMethods setConstrainedFrameSize:];
-[NSUITextViewCommonMethods setNeedsDisplayInRect:avoidAdditionalLayout:];
-[NSUITextViewCommonMethods invalidateTextContainerOrigin];
-[NSUITextViewCommonMethods textContainerInset];
-[NSUITextViewCommonMethods markedTextStyle];
-[NSUITextViewCommonMethods markedRange];
-[NSUITextViewCommonMethods setTextContainer:];
-[NSUITextViewCommonMethods textContainer];
-[NSUITextViewCommonMethods setMarkedRange:];
```
