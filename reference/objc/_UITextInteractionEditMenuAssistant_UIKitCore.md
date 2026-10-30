# `_UITextInteractionEditMenuAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 14 properties, 47 instance methods, 0 class methods

## Instance variables

```
@"NSTimer" _delayedEditMenuTimer;
@"NSNumber" _interactionAssistantViewRespondsShouldShowEditMenu;
B _wasShowingEditMenuBeforeScroll;
@"UITextInteractionAssistant" _interactionAssistant;
@"UITextContextMenuInteraction" _menuInteraction;
@"NSArray" _replacements;
@"UIMenu" _overrideMenu;
```

## Properties

```
@property (T@"UITextInteractionAssistant",R,W,N,V_interactionAssistant) interactionAssistant;
@property (T@"UITextContextMenuInteraction",&,N,V_menuInteraction) menuInteraction;
@property (T@"NSArray",R,N,V_replacements) replacements;
@property (T@"UIMenu",R,N,V_overrideMenu) overrideMenu;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _editMenuTargetRect;
@property (T@"NSArray",R,N) _preferredLayoutRectsForEditMenu;
@property (TB,R,N) _editMenuIsVisible;
@property (TB,R,N) _editMenuIsVisibleOrDismissedRecently;
@property (TB,R,N) _editMenuDismissedRecently;
@property (TB,R,N) _editMenuDismissedByActionSelection;
@property (TB,R,N) _editMenuPrefersPresentationInView;
@property (TB,R,N) _hasTextReplacements;
@property (T@"UIWindow",R,N) _editMenuSourceWindow;
@property (T@"UIView",R,N) _selectionView;
```

## Instance methods

```
-[_UITextInteractionEditMenuAssistant setMenuInteraction:];
-[_UITextInteractionEditMenuAssistant interactionAssistant];
-[_UITextInteractionEditMenuAssistant _presentEditMenuWithPreferredDirection:replacements:];
-[_UITextInteractionEditMenuAssistant _windowCoordinateSpace];
-[_UITextInteractionEditMenuAssistant _presentEditMenuWithPreferredDirection:replacements:overrideMenu:];
-[_UITextInteractionEditMenuAssistant selectionBoundingBox];
-[_UITextInteractionEditMenuAssistant initWithInteractionAssistant:];
-[_UITextInteractionEditMenuAssistant _editMenuPrefersPresentationInView];
-[_UITextInteractionEditMenuAssistant hideSelectionCommands];
-[_UITextInteractionEditMenuAssistant showCalloutBarAfterDelay:];
-[_UITextInteractionEditMenuAssistant _screenCoordinateSpace];
-[_UITextInteractionEditMenuAssistant menuInteraction];
-[_UITextInteractionEditMenuAssistant showSelectionCommandsAfterDelay:];
-[_UITextInteractionEditMenuAssistant _showSelectionCommandsForContextMenu:];
-[_UITextInteractionEditMenuAssistant _selectionView];
-[_UITextInteractionEditMenuAssistant _didReceiveSelectionWillScrollNotification:];
-[_UITextInteractionEditMenuAssistant _isAffectedByScrollNotification:];
-[_UITextInteractionEditMenuAssistant _clippedTargetRect:];
-[_UITextInteractionEditMenuAssistant selectionBoundingBoxForRects:];
-[_UITextInteractionEditMenuAssistant _expandClippingArea:forIdiom:];
-[_UITextInteractionEditMenuAssistant _updateVisibleEditMenuPositionAnimated:];
-[_UITextInteractionEditMenuAssistant calculateReplacementsWithGenerator:andShowAfterDelay:];
-[_UITextInteractionEditMenuAssistant replacements];
-[_UITextInteractionEditMenuAssistant _editMenuTargetRect];
-[_UITextInteractionEditMenuAssistant _updateEditMenuPositionForPreferredArrowDirection:replacements:];
-[_UITextInteractionEditMenuAssistant _presentEditMenuWithPreferredDirection:overrideMenu:];
-[_UITextInteractionEditMenuAssistant _textViewCoordinateSpace];
-[_UITextInteractionEditMenuAssistant _selectionViewCoordinateSpace];
-[_UITextInteractionEditMenuAssistant _hideSelectionCommandsWithReason:];
-[_UITextInteractionEditMenuAssistant showSelectionCommands];
-[_UITextInteractionEditMenuAssistant _editMenuConfigurationForCurrentSelectionWithPreferredArrowDirection:];
-[_UITextInteractionEditMenuAssistant _preferredLayoutRectsForEditMenu];
-[_UITextInteractionEditMenuAssistant _hasTextReplacements];
-[_UITextInteractionEditMenuAssistant _editMenuIsVisible];
-[_UITextInteractionEditMenuAssistant menuElementsForReplacements:];
-[_UITextInteractionEditMenuAssistant _showCommandsWithReplacements:forDictation:afterDelay:];
-[_UITextInteractionEditMenuAssistant showCommandsWithReplacements:];
-[_UITextInteractionEditMenuAssistant _editMenuSourceWindow];
-[_UITextInteractionEditMenuAssistant _editMenuDismissedByActionSelection];
-[_UITextInteractionEditMenuAssistant _editMenuIsVisibleOrDismissedRecently];
-[_UITextInteractionEditMenuAssistant overrideMenu];
-[_UITextInteractionEditMenuAssistant cancelDelayedCommandRequests];
-[_UITextInteractionEditMenuAssistant showReplacementsWithGenerator:forDictation:afterDelay:];
-[_UITextInteractionEditMenuAssistant _showCommandsWithReplacements:isForContextMenu:forDictation:arrowDirection:];
-[_UITextInteractionEditMenuAssistant _editMenuDismissedRecently];
-[_UITextInteractionEditMenuAssistant _editMenuRawTargetRect];
-[_UITextInteractionEditMenuAssistant _didReceiveSelectionDidScrollNotification:];
```
