from manim import *
import numpy as np
import math

class BlackLittermanExplanation(Scene):
    def construct(self):
        # Title sequence
        title = Text("Black-Litterman Portfolio Optimization", font_size=42, color=BLUE)
        subtitle = Text("Combining Market Equilibrium with Investor Views", font_size=28, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Part 1: The Problem with Markowitz
        problem_title = Text("The Problem: Mean-Variance Optimization", font_size=36, color=RED)
        problem_title.to_edge(UP, buff=0.5)
        
        problems = VGroup(
            Text("• Extreme portfolio concentrations", font_size=24),
            Text("• High sensitivity to input estimates", font_size=24),
            Text("• Unintuitive 'garbage in, garbage out'", font_size=24),
            Text("• Difficult to estimate expected returns", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(problem_title, DOWN, buff=0.5)
        
        self.play(Write(problem_title))
        self.wait(1)
        for problem in problems:
            self.play(Write(problem), run_time=0.8)
        self.wait(2)
        
        # Clear for next section
        self.play(FadeOut(problem_title), FadeOut(problems))
        
        # Part 2: The Black-Litterman Solution - FIXED LAYOUT
        solution_title = Text("Black-Litterman Solution: Bayesian Approach", font_size=36, color=GREEN)
        solution_title.to_edge(UP, buff=0.5)
        
        self.play(Write(solution_title))
        self.wait(1)
        
        # Create two columns with proper spacing
        prior_column = VGroup(
            Text("PRIOR", font_size=28, color=BLUE),
            Text("Market Equilibrium", font_size=22),
            Text("Returns", font_size=22),
            Text("• Reverse-engineered", font_size=18),
            Text("  from market caps", font_size=18),
            Text("• Π = δΣw_mkt", font_size=18, color=YELLOW),
            Text("• 'Neutral' starting", font_size=18),
            Text("  point", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(LEFT * 3.2 + UP * 0.5)
        
        views_column = VGroup(
            Text("VIEWS", font_size=28, color=RED),
            Text("Investor Opinions", font_size=22),
            Text("• Absolute or", font_size=18),
            Text("  relative views", font_size=18),
            Text("• Pμ = Q + ε", font_size=18, color=YELLOW),
            Text("• Confidence", font_size=18),
            Text("  levels Ω", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(RIGHT * 3.2 + UP * 0.5)
        
        # Add connecting arrow
        arrow = Arrow(prior_column.get_right() + RIGHT * 0.2, views_column.get_left() + LEFT * 0.2, 
                     color=WHITE, buff=0.3, stroke_width=3)
        combine_text = Text("Bayesian Combination", font_size=20, color=PURPLE).next_to(arrow, UP, buff=0.1)
        
        self.play(Write(prior_column), run_time=1.5)
        self.wait(0.5)
        self.play(Write(views_column), run_time=1.5)
        self.wait(0.5)
        self.play(Create(arrow), Write(combine_text))
        self.wait(2)
        
        # Show the Bayesian formula in two parts with proper positioning
        formula_part1 = MathTex(
            r"E[R] = \left[ (\tau\Sigma)^{-1} + P^T \Omega^{-1} P \right]^{-1}",
            font_size=24
        ).next_to(arrow, DOWN, buff=0.8)
        
        formula_part2 = MathTex(
            r"\left[ (\tau\Sigma)^{-1} \Pi + P^T \Omega^{-1} Q \right]",
            font_size=24
        ).next_to(formula_part1, DOWN, buff=0.1)
        
        self.play(Write(formula_part1), run_time=1.5)
        self.wait(0.5)
        self.play(Write(formula_part2), run_time=1.5)
        self.wait(3)
        
        # Clear for visual demonstration
        self.play(
            FadeOut(prior_column), FadeOut(views_column), 
            FadeOut(arrow), FadeOut(combine_text), 
            FadeOut(formula_part1), FadeOut(formula_part2),
            FadeOut(solution_title)
        )
        
        # Part 3: Visual Demonstration - FIXED AXES LAYOUT
        visual_title = Text("Visualizing the Black-Litterman Process", font_size=32, color=BLUE)
        visual_title.to_edge(UP, buff=0.5)
        self.play(Write(visual_title))
        self.wait(1)
        
        # Create properly scaled axes
        axes = Axes(
            x_range=[-0.05, 0.15, 0.05],
            y_range=[0, 40, 10],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 2},
            x_axis_config={
                "numbers_to_include": [-0.05, 0, 0.05, 0.10, 0.15],
                "numbers_with_elongated_ticks": [-0.05, 0, 0.05, 0.10, 0.15],
                "font_size": 18
            },
            y_axis_config={
                "numbers_to_include": [0, 10, 20, 30, 40],
                "numbers_with_elongated_ticks": [0, 10, 20, 30, 40],
                "font_size": 18
            },
        ).next_to(visual_title, DOWN, buff=0.8)
        
        # Proper axis labeling
        x_label = Text("Expected Return", font_size=20).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("Probability Density", font_size=20).next_to(axes.y_axis, LEFT, buff=0.3)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)
        
        # Distribution curves with proper scaling
        def prior_pdf(x):
            mu_prior = 0.06
            sigma_prior = 0.025
            return 30 * np.exp(-0.5 * ((x - mu_prior) / sigma_prior) ** 2)
        
        prior_curve = axes.plot(prior_pdf, x_range=[-0.05, 0.15], color=BLUE, stroke_width=3)
        prior_label = Text("Market Prior ~N(Π, τΣ)", font_size=16, color=BLUE).next_to(prior_curve, UP, buff=0.2)
        
        self.play(Create(prior_curve), Write(prior_label))
        self.wait(2)
        
        def view_pdf(x):
            mu_view = 0.09
            sigma_view = 0.018
            return 25 * np.exp(-0.5 * ((x - mu_view) / sigma_view) ** 2)
        
        view_curve = axes.plot(view_pdf, x_range=[-0.05, 0.15], color=RED, stroke_width=3)
        view_label = Text("  Investor View ~N(Q, Ω)", font_size=16, color=RED).next_to(view_curve, UP, buff=0.4)
        
        self.play(Create(view_curve), Write(view_label))
        self.wait(2)
        
        def posterior_pdf(x):
            weight_prior = 0.6
            weight_view = 0.4
            return weight_prior * prior_pdf(x) + weight_view * view_pdf(x)
        
        posterior_curve = axes.plot(posterior_pdf, x_range=[-0.05, 0.15], color=PURPLE, stroke_width=4)
        posterior_label = Text("Posterior ~N(E[R], Σ)", font_size=16, color=PURPLE).next_to(posterior_curve, RIGHT, buff=0.6)
        
        self.play(Create(posterior_curve), Write(posterior_label))
        self.wait(3)
        
        # Confidence text
        confidence_text = Text("Higher confidence → Posterior closer to views", font_size=18, color=YELLOW)
        confidence_text.next_to(axes, DOWN, buff=0.4)
        self.play(Write(confidence_text))
        self.wait(2)
        
        # Clean up for final section
        self.play(
            FadeOut(prior_curve), FadeOut(view_curve), FadeOut(posterior_curve),
            FadeOut(prior_label), FadeOut(view_label), FadeOut(posterior_label),
            FadeOut(confidence_text),
            FadeOut(visual_title),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label)
        )
        
        # Part 4: Final benefits - FIXED LAYOUT
        final_title = Text("Result: Stable, Intuitive Portfolios", font_size=32, color=GREEN)
        final_title.to_edge(UP, buff=0.5)
        
        benefits = VGroup(
            Text("• Well-diversified starting point", font_size=22),
            Text("• Controlled tilts based on views", font_size=22),
            Text("• No extreme concentrations", font_size=22),
            Text("• Handles estimation error", font_size=22),
            Text("• Intuitive: views + confidence", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(final_title, DOWN, buff=0.6)
        
        # Add a simple graphic to the right
        graphic_axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=2,
            y_length=2,
            axis_config={"color": WHITE, "stroke_width": 1}
        ).next_to(benefits, RIGHT, buff=1.0)
        
        market_dot = Dot(graphic_axes.c2p(2.5, 2.5), color=BLUE, radius=0.1)
        view_arrow = Arrow(graphic_axes.c2p(2.5, 2.5), graphic_axes.c2p(3.5, 3.5), color=RED, stroke_width=3)
        final_dot = Dot(graphic_axes.c2p(3.2, 3.2), color=PURPLE, radius=0.12)
        
        graphic_group = VGroup(graphic_axes, market_dot, view_arrow, final_dot)
        
        self.play(Write(final_title))
        self.wait(0.5)
        self.play(Write(benefits), run_time=2)
        self.wait(0.5)
        self.play(Create(graphic_group), run_time=1.5)
        self.wait(2)
        
        # Final conclusion
        conclusion = Text("Black-Litterman: Professional's choice for", font_size=22, color=WHITE)
        conclusion2 = Text("balancing market wisdom with active insights", font_size=22, color=YELLOW)
        conclusion2.next_to(conclusion, DOWN, buff=0.1)
        conclusion_group = VGroup(conclusion, conclusion2).next_to(benefits, DOWN, buff=0.8)
        
        self.play(
            FadeOut(final_title), FadeOut(benefits), FadeOut(graphic_group),
            Write(conclusion_group),
            run_time=2
        )
        self.wait(3)
        
        # Final fade out
        self.play(FadeOut(conclusion_group))