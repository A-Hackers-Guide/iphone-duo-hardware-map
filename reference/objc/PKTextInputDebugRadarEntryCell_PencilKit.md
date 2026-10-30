# `PKTextInputDebugRadarEntryCell`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- 13 instance variables, 13 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _includedEntry;
@"<PKTextInputDebugRadarEntryCellDelegate>" _delegate;
@"PKTextInputDebugLogEntry" _logEntry;
q _contentLevel;
q _entryIndex;
@"NSString" _intendedText;
@"UIView" __borderView;
@"UIButton" __includedButton;
@"UIImageView" __drawingImageView;
@"UILabel" __resultTextLabel;
@"UITextField" __intendedResultField;
@"UIView" __lineSeparator;
@"NSLayoutConstraint" __drawingViewAspectRatioConstraint;
```

## Properties

```
@property (T@"UIView",R,N,V__borderView) _borderView;
@property (T@"UIButton",R,N,V__includedButton) _includedButton;
@property (T@"UIImageView",R,N,V__drawingImageView) _drawingImageView;
@property (T@"UILabel",R,N,V__resultTextLabel) _resultTextLabel;
@property (T@"UITextField",R,N,V__intendedResultField) _intendedResultField;
@property (T@"UIView",R,N,V__lineSeparator) _lineSeparator;
@property (T@"NSLayoutConstraint",&,N,V__drawingViewAspectRatioConstraint) _drawingViewAspectRatioConstraint;
@property (T@"<PKTextInputDebugRadarEntryCellDelegate>",W,N,V_delegate) delegate;
@property (T@"PKTextInputDebugLogEntry",R,N,V_logEntry) logEntry;
@property (Tq,R,N,V_contentLevel) contentLevel;
@property (TB,N,V_includedEntry) includedEntry;
@property (Tq,N,V_entryIndex) entryIndex;
@property (T@"NSString",C,N,V_intendedText) intendedText;
```

## Instance methods

```
-[PKTextInputDebugRadarEntryCell _setupViews];
-[PKTextInputDebugRadarEntryCell setDelegate:];
-[PKTextInputDebugRadarEntryCell logEntry];
-[PKTextInputDebugRadarEntryCell delegate];
-[PKTextInputDebugRadarEntryCell initWithFrame:];
-[PKTextInputDebugRadarEntryCell entryIndex];
-[PKTextInputDebugRadarEntryCell setEntryIndex:];
-[PKTextInputDebugRadarEntryCell contentLevel];
-[PKTextInputDebugRadarEntryCell _borderView];
-[PKTextInputDebugRadarEntryCell _includedButton];
-[PKTextInputDebugRadarEntryCell _attributedResultTextWithReferenceString:referenceStringOffset:recognitionResult:affectedRange:resultType:contentLength:];
-[PKTextInputDebugRadarEntryCell _createIncludedButton];
-[PKTextInputDebugRadarEntryCell _createIntendedField];
-[PKTextInputDebugRadarEntryCell _drawingImageView];
-[PKTextInputDebugRadarEntryCell _drawingViewAspectRatioConstraint];
-[PKTextInputDebugRadarEntryCell _handleIncludedButton];
-[PKTextInputDebugRadarEntryCell _handleIntendedFieldChanged];
-[PKTextInputDebugRadarEntryCell _intendedResultField];
-[PKTextInputDebugRadarEntryCell _lineSeparator];
-[PKTextInputDebugRadarEntryCell _resultTextLabel];
-[PKTextInputDebugRadarEntryCell _setIncludedEntry:notifyDelegate:];
-[PKTextInputDebugRadarEntryCell _setIntendedText:notifyDelegate:];
-[PKTextInputDebugRadarEntryCell _updateBorderView];
-[PKTextInputDebugRadarEntryCell _updateDrawingView];
-[PKTextInputDebugRadarEntryCell _updateIncludedButton];
-[PKTextInputDebugRadarEntryCell _updateIntendedTextField];
-[PKTextInputDebugRadarEntryCell _updateResultTextLabel];
-[PKTextInputDebugRadarEntryCell includedEntry];
-[PKTextInputDebugRadarEntryCell intendedText];
-[PKTextInputDebugRadarEntryCell setIncludedEntry:];
-[PKTextInputDebugRadarEntryCell setIntendedText:];
-[PKTextInputDebugRadarEntryCell setLogEntry:contentLevel:];
-[PKTextInputDebugRadarEntryCell set_drawingViewAspectRatioConstraint:];
```
