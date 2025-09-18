from manim import *
import numpy as np

class MeanVariance3DScene(ThreeDScene):
	def construct(self):
		# Axes: x=Risk (Std Dev), y=Return, z=Weight of Asset 1 (for illustration)
		axes = ThreeDAxes(
			x_range=[0, 0.4, 0.1],
			y_range=[0, 0.3, 0.05],
			z_range=[0, 1, 0.2],
			x_length=7,
			y_length=5,
			z_length=4,
			axis_config={"include_tip": True, "numbers_to_exclude": [0]},
		)
		axes_labels = axes.get_axis_labels(
			Tex("Risk ($\\sigma$)").scale(0.7),
			Tex("Return ($\\mu$)").scale(0.7),
			Tex("Weight Asset 1").scale(0.7)
		)
		self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)
		self.add(axes, axes_labels)

		# Generate sample portfolios (for illustration)
		np.random.seed(42)
		n_portfolios = 30
		risks = np.linspace(0.05, 0.35, n_portfolios)
		returns = 0.05 + 0.6 * risks + 0.05 * np.random.randn(n_portfolios)
		weights = np.linspace(0, 1, n_portfolios)

		# Plot sample portfolios
		dots = VGroup()
		for x, y, z in zip(risks, returns, weights):
			dot = Dot3D(point=axes.c2p(x, y, z), radius=0.06, color=BLUE)
			dots.add(dot)
		self.play(Create(dots))

		# Efficient frontier (parabola for illustration)
		frontier_risks = np.linspace(0.07, 0.32, 50)
		frontier_returns = 0.04 + 0.7 * frontier_risks - 0.5 * (frontier_risks-0.18)**2
		frontier_weights = 0.5 + 0.4 * np.sin(4 * np.pi * (frontier_risks-0.07)/0.25)
		frontier = VMobject(color=YELLOW, stroke_width=6)
		frontier.set_points_smoothly([
			axes.c2p(x, y, z)
			for x, y, z in zip(frontier_risks, frontier_returns, frontier_weights)
		])
		self.play(Create(frontier))

		# Highlight a sample optimal portfolio
		opt_idx = np.argmax(frontier_returns)
		opt_point = axes.c2p(frontier_risks[opt_idx], frontier_returns[opt_idx], frontier_weights[opt_idx])
		opt_dot = Dot3D(point=opt_point, radius=0.09, color=RED)
		opt_label = always_redraw(lambda: Tex("Optimal Portfolio", color=RED).scale(0.7).next_to(opt_dot, UP+RIGHT, buff=0.2))
		self.play(FadeIn(opt_dot), FadeIn(opt_label))

		# Add informative text
		info = Tex(r"Mean-Variance Optimization in 3D: \\ ",
				   r"$x$: Risk ($\\sigma$), $y$: Return ($\\mu$), $z$: Weight of Asset 1 \\ ",
				   r"Blue dots: Sample portfolios \\ ",
				   r"Yellow curve: Efficient frontier \\ ",
				   r"Red dot: Optimal portfolio",
				   tex_environment="flushleft"
				  ).scale(0.6).to_corner(UL)
		self.play(Write(info))

		self.wait(3)
