# `PKMathRecognitionItem`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 17 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"PKStrokeGroupItem" _strokeGroupItem;
@"PKStroke" _heroStroke;
@"NSArray" _scrubbableVariables;
@"NSString" _updatedExpression;
d _updateTimestamp;
B _isGraphable;
@"NSArray" _graphableVariables;
@"NSArray" _availableTranscriptionPaths;
B _shouldBeSolved;
B _isEvaluationExpected;
B _isVerticalExpression;
B _shouldSolveMathFlagIsSet;
B _disallowVariableScrubbing;
@"NSString" _expression;
@"NSUUID" _uuid;
d _sortIndex;
@"NSArray" _allTokens;
@"NSNumber" _stableIdentifier;
@"NSNumber" _changeIdentifier;
d _suggestedHeightForResult;
d _suggestedDistanceBetweenDigits;
@"PKMathRecognitionItemAttributes" _attributes;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (TB,R,N,V_shouldBeSolved) shouldBeSolved;
@property (TB,R,N,V_isEvaluationExpected) isEvaluationExpected;
@property (TB,R,N,V_isVerticalExpression) isVerticalExpression;
@property (TB,R,N) isLowConfidenceMath;
@property (T@"NSUUID",R,N) uuid;
@property (T@"NSString",R,N,V_expression) expression;
@property (T@"NSString",R,N) expressionToPresent;
@property (T@"NSArray",R,N) strokes;
@property (T@"NSArray",R,N) triggerStrokes;
@property (T@"NSArray",R,N) symbolStrokes;
@property (T@"NSArray",R,N) tappableStrokes;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds) bounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) boundsForTriggerStrokes;
@property (Td,R,N) sortIndex;
@property (T@"NSArray",R,N) scrubbableVariables;
@property (T@"NSNumber",R,N) strokeGroupIdentifier;
@property (TB,R,N) shouldSolveMathFlagIsSet;
```

## Instance methods

```
-[PKMathRecognitionItem uuid];
-[PKMathRecognitionItem expression];
-[PKMathRecognitionItem sortIndex];
-[PKMathRecognitionItem bounds];
-[PKMathRecognitionItem strokes];
-[PKMathRecognitionItem isEvaluationExpected];
-[PKMathRecognitionItem strokeGroupIdentifier];
-[PKMathRecognitionItem tappableStrokes];
-[PKMathRecognitionItem boundsForTriggerStrokes];
-[PKMathRecognitionItem expressionToPresent];
-[PKMathRecognitionItem isLowConfidenceMath];
-[PKMathRecognitionItem isValidForDrawing:];
-[PKMathRecognitionItem isVerticalExpression];
-[PKMathRecognitionItem scrubbableVariables];
-[PKMathRecognitionItem shouldBeSolved];
-[PKMathRecognitionItem shouldSolveMathFlagIsSet];
-[PKMathRecognitionItem symbolStrokes];
-[PKMathRecognitionItem triggerStrokes];
```
