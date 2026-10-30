# `TCTextCompositionOutput`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 4 properties, 53 instance methods, 1 class methods

## Instance variables

```
@"NSAttributedString" _rewrittenAttributedString;
@"NSArray" _inputLengths;
@"NSArray" _outputLengths;
@"NSArray" _characterExpansions;
@"NSDictionary" _options;
@"TCTextCompositionUserProvidedPreferences" _userProvidedPreferences;
{_NSRange="location"Q"length"Q} _range;
```

## Properties

```
@property (T@"NSString",R,C) rewrittenString;
@property (T{_NSRange=QQ},R,V_range) range;
@property (T@"NSDictionary",R,C,V_options) options;
@property (T@"TCTextCompositionUserProvidedPreferences",R,C,V_userProvidedPreferences) userProvidedPreferences;
```

## Class methods

```
+[TCTextCompositionOutput supportsSecureCoding];
```

## Instance methods

```
-[TCTextCompositionOutput range];
-[TCTextCompositionOutput encodeWithCoder:];
-[TCTextCompositionOutput description];
-[TCTextCompositionOutput initWithCoder:];
-[TCTextCompositionOutput options];
-[TCTextCompositionOutput copyWithZone:];
-[TCTextCompositionOutput initWithComposedString:options:];
-[TCTextCompositionOutput rewrittenString];
-[TCTextCompositionOutput _addDelimiterRunsForParagraph:delimiterRuns:openingDelimeterRuns:closingDelimiterRuns:];
-[TCTextCompositionOutput _addHTMLDelimiterRunsForParagraph:delimiterRuns:openingDelimeterRuns:closingDelimiterRuns:];
-[TCTextCompositionOutput _closingHTMLTags];
-[TCTextCompositionOutput _delimiterCharacterStrings];
-[TCTextCompositionOutput _delimiterStrings];
-[TCTextCompositionOutput _headingFormattingResultsForString:];
-[TCTextCompositionOutput _inlineFormattingResultsForString:];
-[TCTextCompositionOutput _inlineHTMLFormattingResultsForString:];
-[TCTextCompositionOutput _openingHTMLTags];
-[TCTextCompositionOutput _parseOutput:blockTypeArray:rangeArray:];
-[TCTextCompositionOutput _parseTablesOutput:headerArray:rowArray:];
-[TCTextCompositionOutput _tableRowForParagraph:];
-[TCTextCompositionOutput attributedStringByApplyingHeadingFormattingToAttributedString:];
-[TCTextCompositionOutput attributedStringByApplyingInlineFormattingToAttributedString:];
-[TCTextCompositionOutput attributedStringByApplyingInlineHTMLFormattingToAttributedString:];
-[TCTextCompositionOutput attributedStringForMixedOutput:input:tagger:parseLists:parseTables:error:];
-[TCTextCompositionOutput attributedStringForOrderedListOutput:input:tagger:error:];
-[TCTextCompositionOutput attributedStringForResults:input:];
-[TCTextCompositionOutput attributedStringForTablesOutput:input:textAlignmentArray:tagger:error:textModificationBlock:];
-[TCTextCompositionOutput attributedStringForUnorderedListOutput:input:handleTitles:strictFormatting:allowAlternatives:tagger:error:];
-[TCTextCompositionOutput characterExpansions];
-[TCTextCompositionOutput composedAttributedStringWithDefaultAttributes:];
-[TCTextCompositionOutput enumerateRewrittenAttributedStringsWithInput:usingBlock:];
-[TCTextCompositionOutput formatContentForOpenEndedString:paragraphArray:];
-[TCTextCompositionOutput initWithInput:inputString:openEndedString:leadingString:trailingString:writingOptions:resultOptions:tagger:error:];
-[TCTextCompositionOutput initWithInput:inputString:rewrittenString:outputFormatOptions:resultOptions:tagger:];
-[TCTextCompositionOutput initWithInput:listString:resultOptions:tagger:error:];
-[TCTextCompositionOutput initWithInput:results:resultOptions:];
-[TCTextCompositionOutput initWithInput:rewrittenString:];
-[TCTextCompositionOutput initWithInput:rewrittenString:resultOptions:];
-[TCTextCompositionOutput initWithInput:rewrittenString:resultOptions:tagger:];
-[TCTextCompositionOutput initWithInput:rewrittenString:resultOptions:tagger:userProvidedPreferences:];
-[TCTextCompositionOutput initWithInput:rewrittenString:userProvidedPreferences:];
-[TCTextCompositionOutput initWithInput:tableString:resultOptions:tagger:error:textModificationBlock:];
-[TCTextCompositionOutput initWithInput:takeawayString:resultOptions:tagger:error:];
-[TCTextCompositionOutput initWithRewrittenAttributedString:range:inputLengths:outputLengths:options:];
-[TCTextCompositionOutput initWithRewrittenAttributedString:range:inputLengths:outputLengths:options:characterExpansions:];
-[TCTextCompositionOutput initWithRewrittenAttributedString:range:inputLengths:outputLengths:options:characterExpansions:userProvidedPreferences:];
-[TCTextCompositionOutput inputLengths];
-[TCTextCompositionOutput outputLengths];
-[TCTextCompositionOutput prefixForListItemNumber:level:ordered:];
-[TCTextCompositionOutput rewrittenAttributedString];
-[TCTextCompositionOutput rewrittenAttributedStringWithInput:];
-[TCTextCompositionOutput tablesOutputForParagraphArray:textAlignmentArray:];
-[TCTextCompositionOutput userProvidedPreferences];
```
