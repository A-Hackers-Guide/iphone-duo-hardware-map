# `UIMenu`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIMenuElement`
- Protocols: `_UIMenuElementStateObserver`, `_UIIntelligentAssistantEnvironment`
- 19 instance variables, 25 properties, 67 instance methods, 11 class methods

## Instance variables

```
B _hasCustomizedDisplayPreferences;
B _forceAutomaticSelection;
B __surfacesSelectionState;
{?="isPreparedForDisplay"B"hasVisibleSelectedItem"B"hasDeepHierarchy"B"hasAtLeastOneVisibleItem"B"hasVisibleLargePalette"B"hasAccessoryAction"B} _metadata;
@"UIView" _headerView;
q _resolvedElementSize;
q _preferredIntelligentAssistantVisibility;
@"_UICampoActionConfiguration" _preferredIntelligentAssistantConfiguration;
@"UIMenuElement<UIMenuLeaf>" _pinnedFooterElement;
@"NSString" _identifier;
Q _options;
q _preferredElementSize;
@"NSArray" _children;
@"UIMenuDisplayPreferences" _displayPreferences;
@? _headerViewProvider;
Q _behaviorOptions;
@"<UIMenuForcedAutomaticSelectionDelegate>" _forcedAutomaticSelectionDelegate;
@"UIMenuElement<UIMenuLeaf>" __additionalAction;
q _state;
```

## Properties

```
@property (T{?=BBBBBB},N,V_metadata) metadata;
@property (T@?,C,N,V_headerViewProvider) headerViewProvider;
@property (T@"UIView",R,N,V_headerView) headerView;
@property (TB,N,V_forceAutomaticSelection) forceAutomaticSelection;
@property (TQ,N,V_behaviorOptions) behaviorOptions;
@property (T@"<UIMenuForcedAutomaticSelectionDelegate>",W,N,V_forcedAutomaticSelectionDelegate) forcedAutomaticSelectionDelegate;
@property (Tq,N,S_setResolvedElementSize:,V_resolvedElementSize) _resolvedElementSize;
@property (T@"UIMenuElement<UIMenuLeaf>",C,N,S_setAdditionalAction:,V__additionalAction) _additionalAction;
@property (TB,R,N) _hasVisibleChildren;
@property (TB,N,S_setSurfacesSelectionState:,V__surfacesSelectionState) _surfacesSelectionState;
@property (T@"NSArray",R,C,N) _selectedElements;
@property (T@"UIMenuElement<UIMenuLeaf>",&,N,S_setPinnedFooterElement:,V_pinnedFooterElement) _pinnedFooterElement;
@property (Tq,N,V_state) state;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (TQ,R,N,V_options) options;
@property (Tq,N,V_preferredElementSize) preferredElementSize;
@property (T@"NSArray",R,N,V_children) children;
@property (T@"NSArray",R,N) selectedElements;
@property (T@"UIMenuDisplayPreferences",C,N,V_displayPreferences) displayPreferences;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N,S_setPreferredIntelligentAssistantVisibility:,V_preferredIntelligentAssistantVisibility) _preferredIntelligentAssistantVisibility;
@property (T@"_UICampoActionConfiguration",C,N,S_setPreferredIntelligentAssistantConfiguration:,V_preferredIntelligentAssistantConfiguration) _preferredIntelligentAssistantConfiguration;
```

## Class methods

```
+[UIMenu supportsSecureCoding];
+[UIMenu _defaultInlineMenuWithIdentifier:children:];
+[UIMenu _defaultMenuImageNames];
+[UIMenu _defaultMenuTitles];
+[UIMenu _defaultMenuWithIdentifier:children:];
+[UIMenu _defaultMenuWithIdentifier:options:children:];
+[UIMenu _defaultMenusPreferringVisibleImages];
+[UIMenu menuWithChildren:];
+[UIMenu menuWithTitle:children:];
+[UIMenu menuWithTitle:image:identifier:options:children:];
+[UIMenu menuWithTitle:imageName:identifier:options:children:];
```

## Instance methods

```
-[UIMenu recursiveDescription];
-[UIMenu setState:];
-[UIMenu headerView];
-[UIMenu identifier];
-[UIMenu metadata];
-[UIMenu menuByReplacingChildren:];
-[UIMenu children];
-[UIMenu encodeWithCoder:];
-[UIMenu setMetadata:];
-[UIMenu hash];
-[UIMenu description];
-[UIMenu initWithCoder:];
-[UIMenu options];
-[UIMenu copyWithZone:];
-[UIMenu isEqual:];
-[UIMenu state];
-[UIMenu _acceptMenuVisit:commandVisit:actionVisit:deferredElementVisit:];
-[UIMenu _acceptBoolMenuVisit:leafVisit:];
-[UIMenu _resolveElementSizeWithContext:];
-[UIMenu behaviorOptions];
-[UIMenu _acceptBoolMenuVisit:commandVisit:actionVisit:];
-[UIMenu _acceptMenuVisit:leafVisit:];
-[UIMenu _addRecursiveDescriptionForElement:toString:level:];
-[UIMenu _additionalAction];
-[UIMenu _copyPreservingMetadataAndSharingLeafObservers:];
-[UIMenu _copyPreservingMetadataAndSharingLeafObserversIfNeeded];
-[UIMenu _copyWithOptions:];
-[UIMenu _elementStateDidChange:];
-[UIMenu _elementWillPerformAction:];
-[UIMenu _hasGlobalHeader];
-[UIMenu _hasVisibleChildren];
-[UIMenu _menuByReplacingChildren:additionalOptions:];
-[UIMenu _pinnedFooterElement];
-[UIMenu _preferredIntelligentAssistantConfiguration];
-[UIMenu _preferredIntelligentAssistantVisibility];
-[UIMenu _resolvedElementSize];
-[UIMenu _safeCopy];
-[UIMenu _selectedElements];
-[UIMenu _setAdditionalAction:];
-[UIMenu _setPinnedFooterElement:];
-[UIMenu _setPreferredIntelligentAssistantConfiguration:];
-[UIMenu _setPreferredIntelligentAssistantVisibility:];
-[UIMenu _setResolvedElementSize:];
-[UIMenu _setSurfacesSelectionState:];
-[UIMenu _shouldShowSelectionState];
-[UIMenu _surfacesSelectionState];
-[UIMenu addAsStateObserver];
-[UIMenu childElementForElement:];
-[UIMenu displayPreferences];
-[UIMenu establishInitialDefaultSingleSelection];
-[UIMenu forceAutomaticSelection];
-[UIMenu forcedAutomaticSelectionDelegate];
-[UIMenu headerViewProvider];
-[UIMenu initWithMenu:overrideChildren:];
-[UIMenu initWithMenu:overrideChildren:additionalOptions:];
-[UIMenu initWithTitle:image:imageName:identifier:options:children:];
-[UIMenu preferredElementSize];
-[UIMenu recursivelySelectDefaultForcedSelection:];
-[UIMenu removeAsStateObserver];
-[UIMenu selectedElements];
-[UIMenu setBehaviorOptions:];
-[UIMenu setDisplayPreferences:];
-[UIMenu setForceAutomaticSelection:];
-[UIMenu setForcedAutomaticSelectionDelegate:];
-[UIMenu setHeaderViewProvider:];
-[UIMenu setPreferredElementSize:];
-[UIMenu updateChildrenForSingleSelectedElement:];
```
