# Response to reviewers

We thank the editor and the reviewers for their kind comments, and address
their concerns below.

## Response addressing concerns of both reviewers

Both reviewers found the citation style for some URLs jarring, which we agree
with. We attempted to adhere strictly to the PeerJ author guidelines [1], which
stipulate that even URLs should include author, title, and date, and be cited
in the (author, year) format. Having discussed this with the PeerJ editorial
team, we have confirmed that footnotes may be used where appropriate. As such,
we have replaced the more awkward URL citations with footnotes.

## Response to reviewer 1 (Jake Vanderplas)

Jake points out that the paper may not be in-scope for PeerJ, given
reviewer instructions such as ensuring that the paper "clearly define[s] the
research question", has adequate "experimental design", and that the "findings"
are valid. Our academic editor, Shawn Gomez, confirmed that the paper fits
within the scope of PeerJ as a methods/tools paper, and we double-checked this
with the PeerJ editorial team: Peter Binfield himself confirmed that the paper
is in-scope.

> lines 139-140: the GitHub and Google Groups references are a bit confusing.
> Perhaps these should be footnoted URLs rather than dated references? In any
> case, I'd move the references to the end of their respective sentences.
> 
> line 170: the wikipedia reference is confusing.
> 
> line 229: stray closed parenthesis

These have all been corrected as part of the overhaul of our URL citations.

> line 146: "guarantees universal interoperability" is a bit strong. I can't
> think of counterexamples at the moment, but they may exist!

Good point! We have changed the wording of this sentence to "ensures broad
interoperability".

> line 298: it is very difficult to see the mismatch mentioned here in figure
> 5d, given how small it is.

Figures 5d and 5e are more illustrative in nature: we wanted to be clear that
scikit-image currently does not have robust stitching capabilities. The
difference is indeed small and should be visible in the full size image online.

## Response to reviewer 2

> I think a smart 13 year-old can handle complex systems quite well and such an
> achievement does not necessarily demonstrate the shallowness of
> scikit-image's learning curve.

Certainly. We have reworded this passage to state only that scikit-image has a
use in the educational sector.

> The main point which I feel is missing from the manuscript are more details
> on the Section "Library Contents". This is currently very short.

This is by design, because we do not wish for our paper to read like an
instruction manual. We encourage interested readers to visit our online
documentation for details on each module, and have added a suitable reference
to this section (lines 111-112).

> The matplotlib paper should be cited at least once

This has been added (line 66). We have also added citations to SciPy (Figure 3
caption).

> The authors mention "the rising popularity of Python as a scientific
> programming language". I wonder whether they have some data for this claim.

This claim is based on various anecdotal observations, but can be quantified
in various ways that are difficult to cite, such as:

- Attendance at the annual SciPy conference grew 70% year-over-year between
  2012 and 2013, and is expected to grow a further 50% this year.
- Google Trends shows increasing searches for "scipy", "scikit", "pandas
  python", "matplotlib", and other scientific-Python related terms.

We feel that this claim is uncontroversial enough that it does not warrant a
paragraph-long defense. If the reviewer feels strongly about it, we can
certainly add such corroborating evidence to the text.

> Page 6. lines 85-91: I wonder whether this is the most appropriate location
> for this paragraph, it seems awkwardly placed after the "Library Contents"
> section title.

We have renamed the section to "library overview", which we think makes the
location less awkward.

> Page 6/18, line 92: "currently" should mention a specific version and perhaps
> release date to avoid having the paper become outdated and confusing very
> fast.

We have added a version number and date to this sentence (line 92).

> Page 7/18, line 146: I would prefer if "universal interoperability" was
> rephrased to just "interoperability"

As mentioned in our responses to Reviewer 1, we have changed this wording to
"broad interoperability".

> Page 7/18, line 152: I do not think that all the readers will be familiar
> with the pull request interface on GH and a short explanation would be in
> order.

We have added some explanatory sentences and a link to the GitHub pull request
help page (lines 154-159).

> page 8/18, lines 168-173: I found it odd that the Wikipedia "Software
> Version" article was referenced here. I do not understand what claim it is
> backing up.

This reference has been removed. (It intended to link to common versioning
practices such as semantic versioning.)

> the deprecation schedule that the authors describe is very aggressive

We have updated our deprecation schedule in response to this comment. From
version 0.10 onwards, we will maintain deprecation warnings over two minor
versions. We have changed the text to reflect this (lines 176-177).

> scikit-image only wraps IO operations from other packages. This fact should
> be stated explicitly

This is now done (lines 100-101).

> page 16/18. I am sure that the authors could provide some data for the claim
> that their package "has seen significant growth in both adoption and
> contribution." I understand the limitations of rough measures (lines of code,
> number of commits, &c), but they are informative of trends.

We have added a reference to the Ohloh page that tracks repository statistics
for the scikit-image project.

> There is some character encoding errors for the Halchenko & Hanke reference.

These have been fixed.

## Additional differences

In addition to the changes requested by the reviewers, we have added two
entirely new sections: one devoted to comparing other prominent packages for
image analysis (lines 309-358) and one briefly outlining the current roadmap
for the library (lines 360-376).

## References

[1] PeerJ - About - Author instructions: Reference format.
    https://peerj.com/about/author-instructions/#reference-format
    Accessed 2014-05-15.
