arXiv_category_dict = {
    'Computer Science - Artificial Intelligence': 'cs.AI',
    'Computer Science - Hardware Architecture': 'cs.AR',
    'Computer Science - Computational Complexity': 'cs.CC',
    'Computer Science - Computational Engineering, Finance, and Science': 'cs.CE',
    'Computer Science - Computational Geometry': 'cs.CG',
    'Computer Science - Computation and Language': 'cs.CL',
    'Computer Science - Cryptography and Security': 'cs.CR',
    'Computer Science - Computer Vision and Pattern Recognition': 'cs.CV',
    'Computer Science - Computers and Society': 'cs.CY',
    'Computer Science - Databases': 'cs.DB',
    'Computer Science - Distributed, Parallel, and Cluster Computing': 'cs.DC',
    'Computer Science - Digital Libraries': 'cs.DL',
    'Computer Science - Discrete Mathematics': 'cs.DM',
    'Computer Science - Data Structures and Algorithms': 'cs.DS',
    'Computer Science - Emerging Technologies': 'cs.ET',
    'Computer Science - Formal Languages and Automata Theory': 'cs.FL',
    'Computer Science - General Literature': 'cs.GL',
    'Computer Science - Graphics': 'cs.GR',
    'Computer Science - Computer Science and Game Theory': 'cs.GT',
    'Computer Science - Human-Computer Interaction': 'cs.HC',
    'Computer Science - Information Retrieval': 'cs.IR',
    'Computer Science - Information Theory': 'cs.IT',
    'Computer Science - Machine Learning': 'cs.LG',
    'Computer Science - Logic in Computer Science': 'cs.LO',
    'Computer Science - Multiagent Systems': 'cs.MA',
    'Computer Science - Multimedia': 'cs.MM',
    'Computer Science - Mathematical Software': 'cs.MS',
    'Computer Science - Numerical Analysis': 'cs.NA',
    'Computer Science - Neural and Evolutionary Computing': 'cs.NE',
    'Computer Science - Networking and Internet Architecture': 'cs.NI',
    'Computer Science - Other Computer Science': 'cs.OH',
    'Computer Science - Operating Systems': 'cs.OS',
    'Computer Science - Performance': 'cs.PF',
    'Computer Science - Programming Languages': 'cs.PL',
    'Computer Science - Robotics': 'cs.RO',
    'Computer Science - Symbolic Computation': 'cs.SC',
    'Computer Science - Sound': 'cs.SD',
    'Computer Science - Software Engineering': 'cs.SE',
    'Computer Science - Social and Information Networks': 'cs.SI',
    'Computer Science - Systems and Control': 'cs.SY',
    'Economics - Econometrics': 'econ.EM',
    'Economics - General Economics': 'econ.GN',
    'Economics - Theoretical Economics': 'econ.TH',
    'Electrical Engineering and Systems Science - Audio and Speech Processing': 'eess.AS',
    'Electrical Engineering and Systems Science - Image and Video Processing': 'eess.IV',
    'Electrical Engineering and Systems Science - Signal Processing': 'eess.SP',
    'Electrical Engineering and Systems Science - Systems and Control': 'eess.SY',
    'Mathematics - Commutative Algebra': 'math.AC',
    'Mathematics - Algebraic Geometry': 'math.AG',
    'Mathematics - Analysis of PDEs': 'math.AP',
    'Mathematics - Algebraic Topology': 'math.AT',
    'Mathematics - Classical Analysis and ODEs': 'math.CA',
    'Mathematics - Combinatorics': 'math.CO',
    'Mathematics - Category Theory': 'math.CT',
    'Mathematics - Complex Variables': 'math.CV',
    'Mathematics - Differential Geometry': 'math.DG',
    'Mathematics - Dynamical Systems': 'math.DS',
    'Mathematics - Functional Analysis': 'math.FA',
    'Mathematics - General Mathematics': 'math.GM',
    'Mathematics - General Topology': 'math.GN',
    'Mathematics - Group Theory': 'math.GR',
    'Mathematics - Geometric Topology': 'math.GT',
    'Mathematics - History and Overview': 'math.HO',
    'Mathematics - Information Theory': 'math.IT',
    'Mathematics - K-Theory and Homology': 'math.KT',
    'Mathematics - Logic': 'math.LO',
    'Mathematics - Metric Geometry': 'math.MG',
    'Mathematics - Mathematical Physics': 'math.MP',
    'Mathematics - Numerical Analysis': 'math.NA',
    'Mathematics - Number Theory': 'math.NT',
    'Mathematics - Operator Algebras': 'math.OA',
    'Mathematics - Optimization and Control': 'math.OC',
    'Mathematics - Probability': 'math.PR',
    'Mathematics - Quantum Algebra': 'math.QA',
    'Mathematics - Rings and Algebras': 'math.RA',
    'Mathematics - Representation Theory': 'math.RT',
    'Mathematics - Symplectic Geometry': 'math.SG',
    'Mathematics - Spectral Theory': 'math.SP',
    'Mathematics - Statistics Theory': 'math.ST',
    'Physics - Astrophysics - Cosmology and Nongalactic Astrophysics': 'astro-ph.CO',
    'Physics - Astrophysics - Earth and Planetary Astrophysics': 'astro-ph.EP',
    'Physics - Astrophysics - Astrophysics of Galaxies': 'astro-ph.GA',
    'Physics - Astrophysics - High Energy Astrophysical Phenomena': 'astro-ph.HE',
    'Physics - Astrophysics - Instrumentation and Methods for Astrophysics': 'astro-ph.I',
    'Physics - Astrophysics - Solar and Stellar Astrophysics': 'astro-ph.SR',
    'Physics - Condensed Matter - Disordered Systems and Neural Networks': 'cond-mat.dis-nn',
    'Physics - Condensed Matter - Mesoscale and Nanoscale Physics': 'cond-mat.mes-hall',
    'Physics - Condensed Matter - Materials Science': 'cond-mat.mtrl-sci',
    'Physics - Condensed Matter - Other Condensed Matter': 'cond-mat.other',
    'Physics - Condensed Matter - Quantum Gases': 'cond-mat.quant-gas',
    'Physics - Condensed Matter - Soft Condensed Matter': 'cond-mat.soft',
    'Physics - Condensed Matter - Statistical Mechanics': 'cond-mat.stat-mech',
    'Physics - Condensed Matter - Strongly Correlated Electrons': 'cond-mat.str-el',
    'Physics - Condensed Matter - Superconductivity': 'cond-mat.supr-con',
    'Physics - General Relativity and Quantum Cosmology - General Relativity and Quantum Cosmology': 'gr-qc',
    'Physics - High Energy Physics - Experiment - High Energy Physics - Experiment': 'hep-ex',
    'Physics - High Energy Physics - Lattice - High Energy Physics - Lattice': 'hep-lat',
    'Physics - High Energy Physics - Phenomenology - High Energy Physics - Phenomenology': 'hep-ph',
    'Physics - High Energy Physics - Theory - High Energy Physics - Theory': 'hep-th',
    'Physics - Mathematical Physics - Mathematical Physics': 'math-ph',
    'Physics - Nonlinear Sciences - Adaptation and Self-Organizing Systems': 'nlin.AO',
    'Physics - Nonlinear Sciences - Chaotic Dynamics': 'nlin.CD',
    'Physics - Nonlinear Sciences - Cellular Automata and Lattice Gases': 'nlin.CG',
    'Physics - Nonlinear Sciences - Pattern Formation and Solitons': 'nlin.PS',
    'Physics - Nonlinear Sciences - Exactly Solvable and Integrable Systems': 'nlin.SI',
    'Physics - Nuclear Experiment - Nuclear Experiment': 'nucl-ex',
    'Physics - Nuclear Theory - Nuclear Theory': 'nucl-th',
    'Physics - Accelerator Physics': 'physics.acc-ph',
    'Physics - Atmospheric and Oceanic': 'physics.ao-ph',
    'Physics - Applied Physics': 'physics.app-ph',
    'Physics - Atomic and Molecular Clusters': 'physics.atm-clus',
    'Physics - Atomic Physics': 'physics.atom-ph',
    'Physics - Biological Physics': 'physics.bio-ph',
    'Physics - Chemical Physics': 'physics.chem-ph',
    'Physics - Classical Physics': 'physics.class-ph',
    'Physics - Computational Physics': 'physics.comp-ph',
    'Physics - Data Analysis, Statistics and Probability': 'physics.data-an',
    'Physics - Physics Education': 'physics.ed-ph',
    'Physics - Fluid Dynamics': 'physics.flu-dyn',
    'Physics - General Physics': 'physics.gen-ph',
    'Physics - Geophysics': 'physics.geo-ph',
    'Physics - History and Philosophy of Physics': 'physics.hist-ph',
    'Physics - Instrumentation and Detectors': 'physics.ins-det',
    'Physics - Medical Physics': 'physics.med-ph',
    'Physics - Optics': 'physics.optics',
    'Physics - Plasma Physics': 'physics.plasm-ph',
    'Physics - Popular Physics': 'physics.pop-ph',
    'Physics - Physics and Society': 'physics.soc-ph',
    'Physics - Space Physics': 'physics.space-ph',
    'Physics - Quantum Physics - Quantum Physics': 'quant-ph',
    'Quantitative Biology - Biomolecules': 'q-bio.BM',
    'Quantitative Biology - Cell Behavior': 'q-bio.CB',
    'Quantitative Biology - Genomics': 'q-bio.GN',
    'Quantitative Biology - Molecular Networks': 'q-bio.MN',
    'Quantitative Biology - Neurons and Cognition': 'q-bio.NC',
    'Quantitative Biology - Other Quantitative Biology': 'q-bio.OT',
    'Quantitative Biology - Populations and Evolution': 'q-bio.PE',
    'Quantitative Biology - Quantitative Methods': 'q-bio.QM',
    'Quantitative Biology - Subcellular Processes': 'q-bio.SC',
    'Quantitative Biology - Tissues and Organs': 'q-bio.TO',
    'Quantitative Finance - Computational Finance': 'q-fin.CP',
    'Quantitative Finance - Economics': 'q-fin.EC',
    'Quantitative Finance - General Finance': 'q-fin.GN',
    'Quantitative Finance - Mathematical Finance': 'q-fin.MF',
    'Quantitative Finance - Portfolio Management': 'q-fin.PM',
    'Quantitative Finance - Pricing of Securities': 'q-fin.PR',
    'Quantitative Finance - Risk Management': 'q-fin.RM',
    'Quantitative Finance - Statistical Finance': 'q-fin.ST',
    'Quantitative Finance - Trading and Market Microstructure': 'q-fin.TR',
    'Statistics - Applications': 'stat.AP',
    'Statistics - Computation': 'stat.CO',
    'Statistics - Methodology': 'stat.ME',
    'Statistics - Machine Learning': 'stat.ML',
    'Statistics - Other Statistics': 'stat.OT',
    'Statistics - Statistics Theory': 'stat.TH',
}