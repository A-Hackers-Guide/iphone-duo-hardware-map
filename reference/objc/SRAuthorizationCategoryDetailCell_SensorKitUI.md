# `SRAuthorizationCategoryDetailCell`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- 24 instance variables, 24 properties, 45 instance methods, 1 class methods

## Instance variables

```
B _showAppUsage;
B _OBKStyle;
@"UILabel" _categorySubTitleLabel;
@"UILabel" _categoryTitleLabel;
@"UILabel" _appUsageTitleLabel;
@"UILabel" _appUsageBodyLabel;
@"UILabel" _collectedTitleLabel;
@"UILabel" _notCollectedTitleLabel;
@"UILabel" _whenSharedTitleLabel;
@"UILabel" _whatIsSharedTitleLabel;
@"NSArray" _collectedLabels;
@"NSArray" _notCollectedLabels;
q _numberOfCollectedLabels;
q _numberOfNotCollectedLabels;
q _numberOfWhenSharedLabels;
q _numberOfWhatIsSharedLabels;
@"NSArray" _whenSharedLabels;
@"NSArray" _whatIsSharedLabels;
@"UIStackView" _categoryStack;
@"UIStackView" _appUsageStack;
@"UIStackView" _stacks;
@"UIFont" _titleFont;
@"UIFont" _bodyFont;
@"UIColor" _fontColor;
```

## Properties

```
@property (T@"NSArray",&,N,V_collectedLabels) collectedLabels;
@property (T@"NSArray",&,N,V_notCollectedLabels) notCollectedLabels;
@property (T@"NSArray",&,N,V_whenSharedLabels) whenSharedLabels;
@property (T@"NSArray",&,N,V_whatIsSharedLabels) whatIsSharedLabels;
@property (T@"UIStackView",&,N,V_categoryStack) categoryStack;
@property (T@"UIStackView",&,N,V_appUsageStack) appUsageStack;
@property (T@"UIStackView",&,N,V_stacks) stacks;
@property (T@"UIFont",&,N,V_titleFont) titleFont;
@property (T@"UIFont",&,N,V_bodyFont) bodyFont;
@property (T@"UIColor",&,N,V_fontColor) fontColor;
@property (TB,N,V_OBKStyle) OBKStyle;
@property (T@"UILabel",R,N,V_categorySubTitleLabel) categorySubTitleLabel;
@property (T@"UILabel",R,N,V_categoryTitleLabel) categoryTitleLabel;
@property (T@"UILabel",R,N,V_appUsageTitleLabel) appUsageTitleLabel;
@property (T@"UILabel",R,N,V_appUsageBodyLabel) appUsageBodyLabel;
@property (T@"UILabel",R,N,V_collectedTitleLabel) collectedTitleLabel;
@property (T@"UILabel",R,N,V_notCollectedTitleLabel) notCollectedTitleLabel;
@property (T@"UILabel",R,N,V_whenSharedTitleLabel) whenSharedTitleLabel;
@property (T@"UILabel",R,N,V_whatIsSharedTitleLabel) whatIsSharedTitleLabel;
@property (TB,N,V_showAppUsage) showAppUsage;
@property (Tq,N,V_numberOfCollectedLabels) numberOfCollectedLabels;
@property (Tq,N,V_numberOfNotCollectedLabels) numberOfNotCollectedLabels;
@property (Tq,N,V_numberOfWhenSharedLabels) numberOfWhenSharedLabels;
@property (Tq,N,V_numberOfWhatIsSharedLabels) numberOfWhatIsSharedLabels;
```

## Class methods

```
+[SRAuthorizationCategoryDetailCell categoryDetailCellForAuthGroup:bundle:titleFont:bodyFont:textColor:OBKStyle:];
```

## Instance methods

```
-[SRAuthorizationCategoryDetailCell dealloc];
-[SRAuthorizationCategoryDetailCell stacks];
-[SRAuthorizationCategoryDetailCell setStacks:];
-[SRAuthorizationCategoryDetailCell titleFont];
-[SRAuthorizationCategoryDetailCell setTitleFont:];
-[SRAuthorizationCategoryDetailCell fontColor];
-[SRAuthorizationCategoryDetailCell setFontColor:];
-[SRAuthorizationCategoryDetailCell bodyFont];
-[SRAuthorizationCategoryDetailCell setBodyFont:];
-[SRAuthorizationCategoryDetailCell OBKStyle];
-[SRAuthorizationCategoryDetailCell collectedLabels];
-[SRAuthorizationCategoryDetailCell addBulletStackViewForTitleLabel:count:];
-[SRAuthorizationCategoryDetailCell appUsageBodyLabel];
-[SRAuthorizationCategoryDetailCell appUsageStack];
-[SRAuthorizationCategoryDetailCell appUsageTitleLabel];
-[SRAuthorizationCategoryDetailCell categoryStack];
-[SRAuthorizationCategoryDetailCell categorySubTitleLabel];
-[SRAuthorizationCategoryDetailCell categoryTitleLabel];
-[SRAuthorizationCategoryDetailCell collectedTitleLabel];
-[SRAuthorizationCategoryDetailCell dynamicHeightLabel];
-[SRAuthorizationCategoryDetailCell initWithStyle:reuseIdentifier:titleFont:bodyFont:fontColor:OBKStyle:];
-[SRAuthorizationCategoryDetailCell notCollectedLabels];
-[SRAuthorizationCategoryDetailCell notCollectedTitleLabel];
-[SRAuthorizationCategoryDetailCell numberOfCollectedLabels];
-[SRAuthorizationCategoryDetailCell numberOfNotCollectedLabels];
-[SRAuthorizationCategoryDetailCell numberOfWhatIsSharedLabels];
-[SRAuthorizationCategoryDetailCell numberOfWhenSharedLabels];
-[SRAuthorizationCategoryDetailCell setAppUsageStack:];
-[SRAuthorizationCategoryDetailCell setCategoryStack:];
-[SRAuthorizationCategoryDetailCell setCollectedLabels:];
-[SRAuthorizationCategoryDetailCell setNotCollectedLabels:];
-[SRAuthorizationCategoryDetailCell setNumberOfCollectedLabels:];
-[SRAuthorizationCategoryDetailCell setNumberOfNotCollectedLabels:];
-[SRAuthorizationCategoryDetailCell setNumberOfWhatIsSharedLabels:];
-[SRAuthorizationCategoryDetailCell setNumberOfWhenSharedLabels:];
-[SRAuthorizationCategoryDetailCell setOBKStyle:];
-[SRAuthorizationCategoryDetailCell setShowAppUsage:];
-[SRAuthorizationCategoryDetailCell setWhatIsSharedLabels:];
-[SRAuthorizationCategoryDetailCell setWhenSharedLabels:];
-[SRAuthorizationCategoryDetailCell showAppUsage];
-[SRAuthorizationCategoryDetailCell stackViewForSubviews:spacing:];
-[SRAuthorizationCategoryDetailCell whatIsSharedLabels];
-[SRAuthorizationCategoryDetailCell whatIsSharedTitleLabel];
-[SRAuthorizationCategoryDetailCell whenSharedLabels];
-[SRAuthorizationCategoryDetailCell whenSharedTitleLabel];
```
