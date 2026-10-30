# `FBSDisplayLayoutElement`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSXPCCoding`, `BSSettingDescriptionProvider`, `BSDescriptionProviding`, `FBSDisplayLayoutElement`
- 9 instance variables, 13 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _bundleIdentifier;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceFrame;
q _level;
B _fillsDisplayBounds;
B _application;
B _keyboardFocus;
@"BSMutableSettings" _otherSettings;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_referenceFrame) referenceFrame;
@property (Tq,N,V_level) level;
@property (TB,N,V_fillsDisplayBounds) fillsDisplayBounds;
@property (TB,N,GisUIApplicationElement,V_application) UIApplicationElement;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (TB,N,V_keyboardFocus) hasKeyboardFocus;
@property (T@"BSMutableSettings",R,C,N,V_otherSettings) otherSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSDisplayLayoutElement hasKeyboardFocus];
-[FBSDisplayLayoutElement identifier];
-[FBSDisplayLayoutElement succinctDescriptionBuilder];
-[FBSDisplayLayoutElement init];
-[FBSDisplayLayoutElement initWithXPCDictionary:];
-[FBSDisplayLayoutElement referenceFrame];
-[FBSDisplayLayoutElement valueDescriptionForFlag:object:ofSetting:];
-[FBSDisplayLayoutElement bundleIdentifier];
-[FBSDisplayLayoutElement level];
-[FBSDisplayLayoutElement keyDescriptionForSetting:];
-[FBSDisplayLayoutElement descriptionWithMultilinePrefix:];
-[FBSDisplayLayoutElement succinctDescription];
-[FBSDisplayLayoutElement setLevel:];
-[FBSDisplayLayoutElement setIdentifier:];
-[FBSDisplayLayoutElement encodeWithXPCDictionary:];
-[FBSDisplayLayoutElement setFrame:];
-[FBSDisplayLayoutElement hash];
-[FBSDisplayLayoutElement description];
-[FBSDisplayLayoutElement setBundleIdentifier:];
-[FBSDisplayLayoutElement copyWithZone:];
-[FBSDisplayLayoutElement isEqual:];
-[FBSDisplayLayoutElement setReferenceFrame:];
-[FBSDisplayLayoutElement initWithIdentifier:];
-[FBSDisplayLayoutElement fallbackXPCEncodableClass];
-[FBSDisplayLayoutElement descriptionBuilderWithMultilinePrefix:];
-[FBSDisplayLayoutElement frame];
-[FBSDisplayLayoutElement otherSettings];
-[FBSDisplayLayoutElement isUIApplicationElement];
-[FBSDisplayLayoutElement fillsDisplayBounds];
-[FBSDisplayLayoutElement setFillsDisplayBounds:];
-[FBSDisplayLayoutElement setHasKeyboardFocus:];
-[FBSDisplayLayoutElement setOtherSettings:];
-[FBSDisplayLayoutElement setUIApplicationElement:];
```
