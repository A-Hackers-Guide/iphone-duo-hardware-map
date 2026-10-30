# `TPNumberPadKey`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 8 properties, 23 instance methods, 2 class methods

## Instance variables

```
@"UILabel" _digit;
@"UILabel" _letters;
@"UILabel" _secondaryLetters;
@"NSLayoutConstraint" _digitBaseline;
@"NSLayoutConstraint" _letterBaseline;
@"NSLayoutConstraint" _secondaryLetterBaseline;
```

## Properties

```
@property (TB,R,N,GisAsterisk) asterisk;
@property (TB,R,N,GisPound) pound;
@property (T@"UILabel",&,N,V_digit) digit;
@property (T@"UILabel",&,N,V_letters) letters;
@property (T@"UILabel",&,N,V_secondaryLetters) secondaryLetters;
@property (T@"NSLayoutConstraint",&,N,V_digitBaseline) digitBaseline;
@property (T@"NSLayoutConstraint",&,N,V_letterBaseline) letterBaseline;
@property (T@"NSLayoutConstraint",&,N,V_secondaryLetterBaseline) secondaryLetterBaseline;
```

## Class methods

```
+[TPNumberPadKey initialize];
+[TPNumberPadKey absoluteTrackingValueForString:pointSize:unitsPerEm:];
```

## Instance methods

```
-[TPNumberPadKey updateBaselineConstraintConstantsFor:language:showLocalizedLetters:];
-[TPNumberPadKey setDigitBaseline:];
-[TPNumberPadKey setSecondaryLetters:];
-[TPNumberPadKey secondaryLetterFontSizeForScreenSizeCategory:];
-[TPNumberPadKey letters];
-[TPNumberPadKey secondaryLetters];
-[TPNumberPadKey setDigit:];
-[TPNumberPadKey setFontStylesForHighlightState:language:showLocalizedLetters:shouldCenterDigit:fontColor:circleDiameter:isCarPlay:screenSizeCategory:];
-[TPNumberPadKey setLetters:];
-[TPNumberPadKey isAsterisk];
-[TPNumberPadKey doLayoutNow];
-[TPNumberPadKey digitFontSizeForScreenSizeCategory:language:showLocalizedLetters:];
-[TPNumberPadKey letterBaseline];
-[TPNumberPadKey digit];
-[TPNumberPadKey letterFontSizeForScreenSizeCategory:language:showLocalizedLetters:];
-[TPNumberPadKey digitBaselineForDiameter:];
-[TPNumberPadKey isPound];
-[TPNumberPadKey digitBaseline];
-[TPNumberPadKey setDigit:primaryLetters:secondaryLetters:];
-[TPNumberPadKey secondaryLetterBaseline];
-[TPNumberPadKey setSecondaryLetterBaseline:];
-[TPNumberPadKey initWithFrame:];
-[TPNumberPadKey setLetterBaseline:];
```
