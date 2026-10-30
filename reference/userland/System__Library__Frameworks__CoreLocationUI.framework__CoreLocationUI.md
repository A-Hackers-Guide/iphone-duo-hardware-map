# `/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI`

iOS 27.2 dyld shared cache image. Version `3187.0.1.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/CoreText.framework/CoreText`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`
- `/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`
- `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`
- `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

## Objective-C: 3 classes, 5 protocols, 118 methods, 39 properties

### Class pages

Every class and protocol, with its methods: [`CLLocationButton`](../objc/CLLocationButton_CoreLocationUI.md), [`CLLocationButtonDrawing`](../objc/CLLocationButtonDrawing_CoreLocationUI.md), [`CLLocationButtonTag`](../objc/CLLocationButtonTag_CoreLocationUI.md), [`LocationUIProtocol`](../objc/LocationUIProtocol_CoreLocationUI.protocol.md), [`NSCoding`](../objc/NSCoding_CoreLocationUI.protocol.md), [`NSObject`](../objc/NSObject_CoreLocationUI.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_CoreLocationUI.protocol.md), [`UISDrawing`](../objc/UISDrawing_CoreLocationUI.protocol.md)

### Classes

`CLLocationButton`, `CLLocationButtonDrawing`, `CLLocationButtonTag`

### Protocols

`LocationUIProtocol`, `NSCoding`, `NSObject`, `NSSecureCoding`, `UISDrawing`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T{CGSize=dd},R,N) drawingSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) alignmentRect;
@property (T@"<LocationUIProtocol>",R,N) locationUIProxy;
@property (TB,R,N,V_colorsIllegible) colorsIllegible;
@property (TB,R,N,V_alphaInsufficient) alphaInsufficient;
@property (Ti,N,V_controlSize) controlSize;
@property (Tq,N,V_icon) icon;
@property (Tq,N,V_label) label;
@property (Td,N,V_fontSize) fontSize;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T{CGSize=dd},N,V_engravedSize) engravedSize;
@property (T{CGSize=dd},N,V_neededSize) neededSize;
@property (T@"NSString",&,N,V_localizedTitle) localizedTitle;
@property (T@"UISTextLineDrawing",&,N,V_textDrawing) textDrawing;
@property (T@"UISVectorGlyphDrawing",&,N,V_glyphDrawing) glyphDrawing;
@property (TI,R,N,V_secureName) secureName;
@property (T{CGSize=dd},R,N) drawingSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) alignmentRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_fontSize) fontSize;
@property (Tq,N,V_label) label;
@property (Tq,N,V_icon) icon;
@property (T@"UIColor",&,N,V_backgroundColor) backgroundColor;
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (T@"UISSlotStyle",&,N,V_style) style;
@property (TB,N,V_renderedSuccessfully) renderedSuccessfully;
@property (Ti,N,V_controlSize) controlSize;
@property (Td,R,D,N) buttonWidth;
@property (Td,R,D,N) buttonHeight;
```

## Strings (48)

```
LOCATION_BUTTON_SHARE_MY_CURRENT_LOCATION
kCLLocationButtonVersion
kCLLocationButtonCornerRadius
CoreLocationUI
location.fill
Assets
com.apple.locationd.CoreLocationUI
v16@?0@\"NSError\"8
com.apple.corelocation.locationUI
_computeLocationButtonTag %@ %@
LOCATION_BUTTON_CURRENT_LOCATION
LOCATION_BUTTON_SEND_CURRENT_LOCATION
LOCATION_BUTTON_SHARE_CURRENT_LOCATION
location
kCLLocationButtonBackgroundColor
LOCATION_BUTTON_SEND_MY_CURRENT_LOCATION
kCLLocationButtonIcon
kCLLocationButtonLabel
kCLLocationButtonFontSize
v32@?0Q8@\"UISSlotStyle\"16@?<B@?@\"<UISSlotAnyContent>\">24
v16@?0@\"UISSlotRemoteContent\"8
kCLLocationButtonFrame
kCLLocationButtonControlSize
kCLLocationButtonTintColor
v8@?0
CLLocationButton
v24@?0@\"UIView\"8@\"UITraitCollection\"16
v16@?0@\"UISMutableSlotStyle\"8
/System/Library/CoreServices/CoreGlyphs.bundle
#locationButton contrastRatio tintColor-details , cumulativeOpacity: %f tintColorAlpha: %f tintColorEffectiveOpacity: %f fgLuminanceAgainstWhite: %f fgLuminanceAgainstBlack: %f
#locationButton _slotView has been already created
Error: #locationButton failed due to illegible colors
Error: #locationButton failed due to Insufficient Alpha
Error: #locationButton remote-imaging suspended. RemoteSlotContent is null
#locationButton could not localize label text in `%@'
#locationButton neededsize %f %f
Error: #locationButton failed due to insufficient contrastRatio between tintColor and backgroundColor
#locationButton could not find CoreLocationUI bundle for localization
#locationButton xpc service(locationUI) Invalidated
#locationButton sandbox-extension: %@
#locationButton traitCollection: %@ backgroundColor:%@ tintColor:%@
#locationButton skip remote-imaging. tag has zero-size frame
#locationButton localizedText:`%@' localization: `%@'
#locationButton buttonPadding %f %f
Error: #locationButton failed due to inappropriate sizes. needed: %f %f; tag %f %f
#locationButton xpc service(locationUI) Interrupted
#locationButton Error with proxy, error: %@
#locationButton contrastRatio backgroundColor-details , cumulativeOpacity: %f bgColorAlpha: %f bgColorEffectiveOpacity: %f bgLuminanceAgainstWhite: %f bgLuminanceAgainstBlack: %f
```
