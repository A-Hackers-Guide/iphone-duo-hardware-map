# `_UIWebViewportHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 10 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _initialConfigurationHasBeenSentToDelegate;
{_UIWebViewportConfiguration="size"{CGSize="width"d"height"d}"initialScale"f"minimumScale"f"maximumScale"f"allowsUserScaling"B"allowsShrinkToFit"B"avoidsUnsafeArea"B} _defaultConfiguration;
{_UIWebViewportConfiguration="size"{CGSize="width"d"height"d}"initialScale"f"minimumScale"f"maximumScale"f"allowsUserScaling"B"allowsShrinkToFit"B"avoidsUnsafeArea"B} _configuration;
I _webkitDefinedConfigurationFlags;
{CGSize="width"d"height"d} _availableViewSize;
{CGSize="width"d"height"d} _viewportArgumentsSize;
B _widthIsDeviceWidth;
B _heightIsDeviceHeight;
B _isInUpdateBlock;
@"<_UIWebViewportHandlerDelegate>" _delegate;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _documentBounds;
```

## Properties

```
@property (T@"<_UIWebViewportHandlerDelegate>",N,V_delegate) delegate;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_documentBounds) documentBounds;
@property (T{CGSize=dd},R,N,V_availableViewSize) availableViewSize;
@property (Tf,R,N) initialScale;
@property (Tf,R,N) minimumScale;
@property (Tf,R,N) maximumScale;
@property (TB,R,N) allowsUserScaling;
@property (TI,R,N,V_webkitDefinedConfigurationFlags) webkitDefinedConfigurationFlags;
@property (TB,R,N) avoidsUnsafeArea;
@property (T{_UIWebViewportConfiguration={CGSize=dd}fffBBB},R,N) rawViewConfiguration;
```

## Instance methods

```
-[_UIWebViewportHandler maximumScale];
-[_UIWebViewportHandler minimumScale];
-[_UIWebViewportHandler update:];
-[_UIWebViewportHandler initialScale];
-[_UIWebViewportHandler setDelegate:];
-[_UIWebViewportHandler delegate];
-[_UIWebViewportHandler _resolveViewSizeRelativeLengths];
-[_UIWebViewportHandler webkitDefinedConfigurationFlags];
-[_UIWebViewportHandler allowsUserScaling];
-[_UIWebViewportHandler applyWebKitViewportArgumentsSize:initialScale:minimumScale:maximumScale:allowsUserScaling:allowsShrinkToFit:viewportFit:];
-[_UIWebViewportHandler availableViewSize];
-[_UIWebViewportHandler avoidsUnsafeArea];
-[_UIWebViewportHandler clearWebKitViewportConfigurationFlags];
-[_UIWebViewportHandler documentBounds];
-[_UIWebViewportHandler integralInitialScale];
-[_UIWebViewportHandler integralScaleForScale:keepingPointFixed:];
-[_UIWebViewportHandler minimumScaleForViewSize:];
-[_UIWebViewportHandler overrideViewportConfiguration:];
-[_UIWebViewportHandler rawViewConfiguration];
-[_UIWebViewportHandler resetViewportConfiguration:];
-[_UIWebViewportHandler setAvailableViewSize:updateConfigurationSize:];
-[_UIWebViewportHandler setDocumentBounds:];
-[_UIWebViewportHandler shouldIgnoreHorizontalScalingConstraints];
-[_UIWebViewportHandler shouldIgnoreScalingConstraints];
-[_UIWebViewportHandler shouldIgnoreVerticalScalingConstraints];
-[_UIWebViewportHandler viewportHeight];
-[_UIWebViewportHandler viewportWidth];
```
